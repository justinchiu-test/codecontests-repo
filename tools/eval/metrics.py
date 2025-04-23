"""
Metrics tracking tools for evaluating code quality and improvements.

This module provides utilities to track and compare various metrics between
original and refactored solutions, including logical lines of code (LLOC),
log probabilities, and code reduction.
"""
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union

from tools.eval.loc import count_lloc_directory, summarize_lloc
from tools.eval.log_prob import get_log_prob_for_directory, summarize_log_probs


def calculate_all_metrics(
    directory: Union[str, Path],
    api_key: Optional[str] = None,
    exclude_dirs: Optional[List[str]] = None,
) -> Dict:
    """
    Calculate all metrics for a directory of code files.

    Args:
        directory: Path to the directory
        api_key: API key for language model service
        exclude_dirs: Directories to exclude from analysis

    Returns:
        Dictionary with all metrics
    """
    directory = Path(directory)
    exclude_dirs = exclude_dirs or ["__pycache__", ".git", ".venv", "venv", "env"]

    # Get logical lines of code
    lloc_counts = count_lloc_directory(directory, exclude_dirs=set(exclude_dirs))
    lloc_summary = summarize_lloc(lloc_counts)

    # Get log probabilities (if API key is provided)
    log_probs = {}
    log_prob_summary = {}

    if api_key:
        try:
            log_probs = get_log_prob_for_directory(
                directory, exclude_dirs=set(exclude_dirs), api_key=api_key
            )
            log_prob_summary = summarize_log_probs(log_probs)
        except Exception as e:
            print(f"Warning: Failed to calculate log probabilities: {e}")

    # Combine metrics
    return {"lloc": lloc_summary, "log_prob": log_prob_summary}


def compare_metrics(
    original_dir: Union[str, Path],
    refactored_dir: Union[str, Path],
    api_key: Optional[str] = None,
    exclude_dirs: Optional[List[str]] = None,
) -> Dict:
    """
    Compare metrics between original and refactored code.

    Args:
        original_dir: Directory with original code
        refactored_dir: Directory with refactored code
        api_key: API key for language model service
        exclude_dirs: Directories to exclude from analysis

    Returns:
        Dictionary with comparison results
    """
    original_metrics = calculate_all_metrics(original_dir, api_key, exclude_dirs)
    refactored_metrics = calculate_all_metrics(refactored_dir, api_key, exclude_dirs)

    # Calculate improvements
    improvements = {}

    # LLOC improvements
    original_lloc = original_metrics["lloc"]["total_lloc"]
    refactored_lloc = refactored_metrics["lloc"]["total_lloc"]

    lloc_change = refactored_lloc - original_lloc
    lloc_pct_change = (lloc_change / original_lloc * 100) if original_lloc > 0 else 0

    improvements["lloc"] = {
        "absolute_change": lloc_change,
        "percentage_change": lloc_pct_change,
    }

    # Log probability improvements (if available)
    if original_metrics["log_prob"] and refactored_metrics["log_prob"]:
        original_avg_log_prob = original_metrics["log_prob"][
            "average_log_prob_per_token"
        ]
        refactored_avg_log_prob = refactored_metrics["log_prob"][
            "average_log_prob_per_token"
        ]

        log_prob_change = refactored_avg_log_prob - original_avg_log_prob

        improvements["log_prob"] = {"average_log_prob_change": log_prob_change}

    return {
        "original": original_metrics,
        "refactored": refactored_metrics,
        "improvements": improvements,
    }


def save_metrics(metrics: Dict, output_file: Union[str, Path]):
    """
    Save metrics to a JSON file.

    Args:
        metrics: Dictionary with metrics
        output_file: Path to the output file
    """
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)


def load_metrics(input_file: Union[str, Path]) -> Dict:
    """
    Load metrics from a JSON file.

    Args:
        input_file: Path to the input file

    Returns:
        Dictionary with metrics
    """
    input_file = Path(input_file)

    if not input_file.exists():
        raise FileNotFoundError(f"Metrics file not found: {input_file}")

    with open(input_file, "r", encoding="utf-8") as f:
        return json.load(f)


def print_metrics_summary(metrics: Dict):
    """
    Print a summary of metrics.

    Args:
        metrics: Dictionary with metrics
    """
    print("Code Metrics Summary")
    print("===================")

    # LLOC metrics
    lloc = metrics.get("lloc", {})
    print(f"\nLogical Lines of Code (LLOC): {lloc.get('total_lloc', 'N/A')}")
    print(f"Files analyzed: {lloc.get('file_count', 'N/A')}")

    # Directory breakdown
    if "directories" in lloc:
        print("\nLLOC by Directory:")
        for dir_name, dir_lloc in sorted(lloc["directories"].items()):
            print(f"  {dir_name}: {dir_lloc}")

    # Log probability metrics
    log_prob = metrics.get("log_prob", {})
    if log_prob:
        print("\nLog Probability:")
        print(f"Total log probability: {log_prob.get('total_log_prob', 'N/A')}")
        print(
            f"Average log prob per token: {log_prob.get('average_log_prob_per_token', 'N/A')}"
        )
        print(f"Total tokens: {log_prob.get('total_tokens', 'N/A')}")


def print_comparison_summary(comparison: Dict):
    """
    Print a summary of metrics comparison.

    Args:
        comparison: Dictionary with comparison results
    """
    print("Metrics Comparison Summary")
    print("=========================")

    # Original metrics
    original = comparison.get("original", {})
    original_lloc = original.get("lloc", {}).get("total_lloc", "N/A")

    # Refactored metrics
    refactored = comparison.get("refactored", {})
    refactored_lloc = refactored.get("lloc", {}).get("total_lloc", "N/A")

    # Improvements
    improvements = comparison.get("improvements", {})
    lloc_change = improvements.get("lloc", {}).get("absolute_change", "N/A")
    lloc_pct_change = improvements.get("lloc", {}).get("percentage_change", "N/A")

    print("\nLogical Lines of Code (LLOC):")
    print(f"  Original: {original_lloc}")
    print(f"  Refactored: {refactored_lloc}")
    print(f"  Change: {lloc_change} lines ({lloc_pct_change:.2f}%)")

    # Log probability improvements (if available)
    if "log_prob" in improvements:
        original_avg_log_prob = original.get("log_prob", {}).get(
            "average_log_prob_per_token", "N/A"
        )
        refactored_avg_log_prob = refactored.get("log_prob", {}).get(
            "average_log_prob_per_token", "N/A"
        )
        log_prob_change = improvements.get("log_prob", {}).get(
            "average_log_prob_change", "N/A"
        )

        print("\nLog Probability (avg per token):")
        print(f"  Original: {original_avg_log_prob}")
        print(f"  Refactored: {refactored_avg_log_prob}")
        print(f"  Change: {log_prob_change}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Calculate metrics for a single directory:")
        print(
            "    python metrics.py analyze <directory> [--api-key KEY] [--output FILE]"
        )
        print("")
        print("  Compare metrics between original and refactored code:")
        print(
            "    python metrics.py compare <original_dir> <refactored_dir> [--api-key KEY] [--output FILE]"
        )
        print("")
        print("  Load and display metrics from a file:")
        print("    python metrics.py load <metrics_file>")
        sys.exit(1)

    command = sys.argv[1]

    # Extract optional arguments
    api_key = None
    output_file = None

    for i, arg in enumerate(sys.argv):
        if arg == "--api-key" and i + 1 < len(sys.argv):
            api_key = sys.argv[i + 1]
        elif arg == "--output" and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]

    try:
        if command == "analyze" and len(sys.argv) >= 3:
            directory = sys.argv[2]
            metrics = calculate_all_metrics(directory, api_key)

            print_metrics_summary(metrics)

            if output_file:
                save_metrics(metrics, output_file)
                print(f"\nMetrics saved to: {output_file}")

        elif command == "compare" and len(sys.argv) >= 4:
            original_dir = sys.argv[2]
            refactored_dir = sys.argv[3]

            comparison = compare_metrics(original_dir, refactored_dir, api_key)

            print_comparison_summary(comparison)

            if output_file:
                save_metrics(comparison, output_file)
                print(f"\nComparison saved to: {output_file}")

        elif command == "load" and len(sys.argv) >= 3:
            metrics_file = sys.argv[2]
            metrics = load_metrics(metrics_file)

            if "improvements" in metrics:
                print_comparison_summary(metrics)
            else:
                print_metrics_summary(metrics)

        else:
            print(f"Unknown command or insufficient arguments: {command}")
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
