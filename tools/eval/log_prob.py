"""
Tools for calculating log probability of code files using TogetherAI API with Qwen 2.5 Coder 32B.

This module provides utilities to measure how "predictable" code is from a
language model perspective. Lower log probability (closer to 0) indicates
more "natural" or probable code according to the model.
"""

import json
import os
import sys
import time
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union

import requests
from tqdm import tqdm

# Default model
DEFAULT_MODEL = "Qwen/Qwen2.5-Coder-32B"
TOGETHER_API_URL = "https://api.together.xyz/v1/completions"


def get_log_prob_for_file(file_path: Union[str, Path], api_key: Optional[str] = None) -> Tuple[float, int]:
    """
    Calculate log probability for a Python file using TogetherAI API with Qwen 2.5 Coder 32B.

    Args:
        file_path: Path to the Python file
        api_key: TogetherAI API key

    Returns:
        Tuple of (log_probability, token_count)
    """
    file_path = Path(file_path)
    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract API key from environment if not provided
    if api_key is None:
        api_key = os.environ.get("TOGETHER_API_KEY")
        if api_key is None:
            raise ValueError("API key must be provided or set as TOGETHER_API_KEY environment variable")

    # Calculate log probability using the API
    return _calculate_log_prob_api(content, api_key)


@lru_cache(maxsize=100)
def _calculate_log_prob_api(content: str, api_key: str) -> Tuple[float, int]:
    """
    Calculate log probability using TogetherAI API with Qwen 2.5 Coder 32B.

    Args:
        content: Code content to calculate log probability for
        api_key: TogetherAI API key

    Returns:
        Tuple of (log_probability, token_count)
    """
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    data = {
        "model": DEFAULT_MODEL,
        "prompt": content,
        "logprobs": True,
        "max_tokens": 1,  # Just need the token probabilities, not generating new tokens
        "temperature": 0,
        "top_p": 1,
    }

    response = requests.post(TOGETHER_API_URL, headers=headers, json=data)

    if response.status_code != 200:
        raise ValueError(f"API request failed with status code {response.status_code}: {response.text}")

    response_data = response.json()

    # Extract logprobs from response
    logprobs = response_data.get("logprobs", {})
    token_logprobs = logprobs.get("token_logprobs", [])

    # Sum up the log probabilities
    total_log_prob = sum(lp for lp in token_logprobs if lp is not None)
    token_count = len(token_logprobs)

    return total_log_prob, token_count


def get_log_prob_for_directory(
    directory: Union[str, Path],
    exclude_dirs: Optional[Set[str]] = None,
    include_patterns: Optional[List[str]] = None,
    api_key: Optional[str] = None,
    batch_size: int = 5,
    delay_seconds: float = 1.0,
) -> Dict[str, Tuple[float, int]]:
    """
    Calculate log probability for all Python files in a directory.

    Args:
        directory: Path to the directory
        exclude_dirs: Set of directory names to exclude
        include_patterns: List of glob patterns to include (e.g., ["**/*.py"])
        api_key: TogetherAI API key
        batch_size: Number of files to process before adding a delay
        delay_seconds: Delay in seconds between batches to avoid API rate limits

    Returns:
        Dictionary mapping file paths to tuples of (log_probability, token_count)
    """
    directory = Path(directory)
    if not directory.exists() or not directory.is_dir():
        raise FileNotFoundError(f"Directory not found: {directory}")

    exclude_dirs = exclude_dirs or {"__pycache__", ".git", ".venv", "venv", "env"}
    include_patterns = include_patterns or ["**/*.py"]

    log_probs = {}
    files_processed = 0

    # Process all files matching the include patterns
    for pattern in include_patterns:
        file_paths = list(directory.glob(pattern))

        # Skip directories in the exclude list
        file_paths = [
            fp for fp in file_paths if fp.is_file() and not any(exclude_dir in fp.parts for exclude_dir in exclude_dirs)
        ]

        file_iterator = tqdm(file_paths, desc="Calculating log probabilities")

        for file_path in file_iterator:
            try:
                log_prob, token_count = get_log_prob_for_file(file_path, api_key)
                log_probs[str(file_path.relative_to(directory))] = (
                    log_prob,
                    token_count,
                )

                # Add delay between batches to avoid API rate limits
                files_processed += 1
                if files_processed % batch_size == 0:
                    time.sleep(delay_seconds)

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    return log_probs


def summarize_log_probs(
    log_probs: Dict[str, Tuple[float, int]], group_by_directory: bool = True
) -> Dict[str, Union[float, int, Dict[str, Dict[str, Union[float, int]]]]]:
    """
    Summarize log probability results, optionally grouping by directory.

    Args:
        log_probs: Dictionary mapping file paths to tuples of (log_probability, token_count)
        group_by_directory: Whether to group results by directory

    Returns:
        Dictionary with summary statistics
    """
    total_log_prob = sum(lp for lp, _ in log_probs.values())
    total_tokens = sum(tc for _, tc in log_probs.values())

    summary: Dict[str, Union[float, int, Dict[str, Dict[str, Union[float, int]]]]] = {
        "total_log_prob": total_log_prob,
        "total_tokens": total_tokens,
        "average_log_prob_per_token": total_log_prob / total_tokens if total_tokens > 0 else 0,
        "file_count": len(log_probs),
    }

    if group_by_directory:
        directories: Dict[str, Dict[str, Union[float, int]]] = {}
        for file_path, (log_prob, token_count) in log_probs.items():
            directory = os.path.dirname(file_path) or "."

            if directory not in directories:
                directories[directory] = {"log_prob": 0.0, "tokens": 0}

            directories[directory]["log_prob"] = directories[directory]["log_prob"] + log_prob
            directories[directory]["tokens"] = directories[directory]["tokens"] + token_count

        # Calculate average log prob per token for each directory
        for dir_data in directories.values():
            log_prob_val = float(dir_data["log_prob"])
            token_count_val = int(dir_data["tokens"])
            dir_data["avg_log_prob_per_token"] = log_prob_val / token_count_val if token_count_val > 0 else 0.0

        summary["directories"] = directories

    return summary


def compare_solutions(
    original_dir: Union[str, Path],
    refactored_dir: Union[str, Path],
    api_key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Compare log probabilities between original and refactored solutions.

    Args:
        original_dir: Directory with original solutions
        refactored_dir: Directory with refactored solutions
        api_key: TogetherAI API key

    Returns:
        Dictionary with comparison results
    """
    original_log_probs = get_log_prob_for_directory(original_dir, api_key=api_key)
    refactored_log_probs = get_log_prob_for_directory(refactored_dir, api_key=api_key)

    original_summary = summarize_log_probs(original_log_probs)
    refactored_summary = summarize_log_probs(refactored_log_probs)

    # Extract values safely
    orig_log_prob = 0.0
    if isinstance(original_summary.get("total_log_prob"), (int, float)):
        orig_log_prob = float(original_summary["total_log_prob"])  # type: ignore

    refact_log_prob = 0.0
    if isinstance(refactored_summary.get("total_log_prob"), (int, float)):
        refact_log_prob = float(refactored_summary["total_log_prob"])  # type: ignore

    orig_avg_log_prob = 0.0
    if isinstance(original_summary.get("average_log_prob_per_token"), (int, float)):
        orig_avg_log_prob = float(original_summary["average_log_prob_per_token"])  # type: ignore

    refact_avg_log_prob = 0.0
    if isinstance(refactored_summary.get("average_log_prob_per_token"), (int, float)):
        refact_avg_log_prob = float(refactored_summary["average_log_prob_per_token"])  # type: ignore

    orig_tokens = 0
    if isinstance(original_summary.get("total_tokens"), (int, float)):
        orig_tokens = int(original_summary["total_tokens"])  # type: ignore

    refact_tokens = 0
    if isinstance(refactored_summary.get("total_tokens"), (int, float)):
        refact_tokens = int(refactored_summary["total_tokens"])  # type: ignore

    # Calculate improvement metrics
    improvement: Dict[str, Union[float, int]] = {
        "total_log_prob_change": refact_log_prob - orig_log_prob,
        "avg_log_prob_per_token_change": refact_avg_log_prob - orig_avg_log_prob,
        "total_tokens_change": refact_tokens - orig_tokens,
        "token_reduction_percentage": ((orig_tokens - refact_tokens) / orig_tokens * 100 if orig_tokens > 0 else 0.0),
    }

    return {
        "original": original_summary,
        "refactored": refactored_summary,
        "improvement": improvement,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_prob.py <directory> [--json] [--api-key KEY] [--compare REFACTORED_DIR]")
        sys.exit(1)

    directory = sys.argv[1]
    output_json = "--json" in sys.argv

    # Extract optional arguments
    api_key = None
    compare_dir = None

    for i, arg in enumerate(sys.argv):
        if arg == "--api-key" and i + 1 < len(sys.argv):
            api_key = sys.argv[i + 1]
        elif arg == "--compare" and i + 1 < len(sys.argv):
            compare_dir = sys.argv[i + 1]

    try:
        if compare_dir:
            # Compare original and refactored solutions
            results = compare_solutions(directory, compare_dir, api_key)

            if output_json:
                print(json.dumps(results, indent=2))
            else:
                print("Original solutions:")
                print(f"  Total log probability: {results['original']['total_log_prob']}")
                print(f"  Total tokens: {results['original']['total_tokens']}")
                print(f"  Average log prob per token: {results['original']['average_log_prob_per_token']}")

                print("\nRefactored solutions:")
                print(f"  Total log probability: {results['refactored']['total_log_prob']}")
                print(f"  Total tokens: {results['refactored']['total_tokens']}")
                print(f"  Average log prob per token: {results['refactored']['average_log_prob_per_token']}")

                print("\nImprovement:")
                print(f"  Log probability change: {results['improvement']['total_log_prob_change']}")
                print(f"  Average log prob per token change: {results['improvement']['avg_log_prob_per_token_change']}")
                print(f"  Token reduction: {results['improvement']['total_tokens_change']} tokens")
                print(f"  Token reduction percentage: {results['improvement']['token_reduction_percentage']:.2f}%")
        else:
            # Process a single directory
            log_probs = get_log_prob_for_directory(directory, api_key=api_key)
            summary = summarize_log_probs(log_probs)

            if output_json:
                print(json.dumps(summary, indent=2))
            else:
                print(f"Total log probability: {summary['total_log_prob']}")
                print(f"Total tokens: {summary['total_tokens']}")
                print(f"Average log prob per token: {summary['average_log_prob_per_token']}")
                print(f"Files processed: {summary['file_count']}")

                if "directories" in summary:
                    print("\nDirectory breakdown:")
                    directories = summary["directories"]
                    if isinstance(directories, dict):
                        for dir_name, data in sorted(directories.items()):
                            if isinstance(data, dict):
                                print(f"  {dir_name}:")
                                print(f"    Log prob: {data.get('log_prob', 'N/A')}")
                                print(f"    Tokens: {data.get('tokens', 'N/A')}")
                                print(f"    Avg log prob per token: {data.get('avg_log_prob_per_token', 'N/A')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
