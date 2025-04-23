"""
Process the code_contests dataset and format problems.

This script:
1. Loads problems from the code_contests dataset
2. Creates standardized problem directories in problems/
3. Generates PROBLEM.md, main.py, and test files
4. Creates run.sh script for each problem
"""
import logging
from pathlib import Path
from typing import List, Optional

from datasets import load_dataset
from pydantic import ValidationError

from tools.formatter.problem_md import generate_problem_md
from tools.formatter.script_sh import generate_run_script
from tools.models.dataset import DatasetProblem

# Import the models
from tools.models.problem import Problem, TestCase

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Constants
DATASET_NAME = "deepmind/code_contests"
REPO_ROOT = Path(__file__).resolve().parents[2]
PROBLEMS_DIR = REPO_ROOT / "problems"


def get_problem_id(name: str, index: int) -> str:
    """
    Generate a unique problem ID based on name and index.

    Args:
        name: Problem name
        index: Problem index in dataset

    Returns:
        Sanitized problem ID
    """
    # Sanitize name to create a valid directory name
    sanitized = name.lower().replace(" ", "_")
    sanitized = "".join(c for c in sanitized if c.isalnum() or c == "_")

    # Add index to ensure uniqueness
    return f"{sanitized}_{index}"


def extract_python_solution(problem: DatasetProblem) -> Optional[str]:
    """
    Extract a Python 3 solution from the problem's solutions.
    Only returns Python 3 solutions, skipping Python 2 solutions.

    Args:
        problem: Problem from the dataset as a Pydantic model

    Returns:
        Python 3 solution code or None if not found
    """
    # Get Python 3 solution from the model
    python3_solution = problem.get_python3_solution()

    if python3_solution:
        logger.info(f"Found Python 3 solution for problem: {problem.name}")
        return python3_solution

    # If no Python 3 solution, skip this problem
    logger.warning(f"No Python 3 solution found for problem: {problem.name}, skipping")
    return None


def create_test_files(
    problem_dir: Path, test_inputs: List[str], test_outputs: List[str]
) -> int:
    """
    Create test input and output files in the problem directory.

    Args:
        problem_dir: Path to the problem directory
        test_inputs: List of test input strings
        test_outputs: List of test output strings

    Returns:
        Number of test cases created
    """
    tests_dir = problem_dir / "tests"
    tests_dir.mkdir(exist_ok=True)

    # Create input and output files
    for i, (input_text, output_text) in enumerate(zip(test_inputs, test_outputs), 1):
        input_path = tests_dir / f"input_{i}.txt"
        output_path = tests_dir / f"output_{i}.txt"

        with open(input_path, "w") as f:
            f.write(input_text.strip())

        with open(output_path, "w") as f:
            f.write(output_text.strip())

    return min(len(test_inputs), len(test_outputs))


def process_problem(dataset_problem: DatasetProblem, index: int) -> bool:
    """
    Process a single problem and create its directory structure.

    Args:
        dataset_problem: Problem from the dataset as a Pydantic model
        index: Problem index for unique ID generation

    Returns:
        True if processing succeeded, False otherwise
    """
    try:
        name = dataset_problem.name
        problem_id = get_problem_id(name, index)

        # Create problem directory
        problem_dir = PROBLEMS_DIR / problem_id
        problem_dir.mkdir(parents=True, exist_ok=True)

        # Extract Python solution
        solution_code = extract_python_solution(dataset_problem)
        if not solution_code:
            # Skip problems without Python solutions
            logger.warning(f"Skipping problem {name} due to missing Python solution")
            return False

        # Write main.py with solution code
        with open(problem_dir / "main.py", "w") as f:
            # Add shebang line
            f.write("#!/usr/bin/env python3\n\n")
            # Write the Python 3 solution directly
            f.write(solution_code)

        # Get all test cases
        test_case_dicts = dataset_problem.get_all_test_cases(min_test_cases=3)

        # Skip if no test cases
        if not test_case_dicts:
            logger.warning(f"Skipping problem {name} due to missing test cases")
            return False

        # Prepare input and output lists for test file creation
        all_inputs = [tc["input"] for tc in test_case_dicts]
        all_outputs = [tc["output"] for tc in test_case_dicts]

        # Create test cases for the problem model
        test_cases = [
            TestCase(input=inp, output=out, time_limit_ms=30000, memory_limit_mb=512)
            for inp, out in zip(all_inputs, all_outputs)
        ]

        # Get difficulty and source as strings
        difficulty_str = dataset_problem.get_difficulty_name()
        source_name = dataset_problem.get_source_name()

        # Get tags/categories
        tags = dataset_problem.cf_tags

        # Create Problem model for our system
        problem_model = Problem(
            id=problem_id,
            name=name,
            description=dataset_problem.description,
            category=tags,
            difficulty=difficulty_str,
            test_cases=test_cases,
            source=source_name,
        )

        # Generate PROBLEM.md
        generate_problem_md(problem_model, problem_dir)

        # Create test files
        num_tests = create_test_files(problem_dir, all_inputs, all_outputs)

        # Generate run.sh script
        generate_run_script(problem_id, problem_dir)

        logger.info(f"Processed problem: {problem_id} with {num_tests} test cases")
        return True

    except Exception as e:
        logger.error(f"Error processing problem {index}: {e}")
        return False


def main():
    """Main entry point for processing problems."""
    # Ensure problems directory exists and it's empty
    PROBLEMS_DIR.mkdir(parents=True, exist_ok=True)

    # Load dataset
    logger.info(f"Loading dataset: {DATASET_NAME}")
    dataset = load_dataset(DATASET_NAME)

    # Get problems from training set
    # We need to type-ignore this because the Dataset class doesn't have proper type annotations
    train_dataset = dataset["train"]  # type: ignore

    # Set target for graph problems
    target_problems = 100  # Target number of graph problems to process

    logger.info("Searching for graph problems with Python 3 solutions")
    logger.info(f"Target: {target_problems} graph problems with Python 3 solutions")

    successful = 0
    attempted = 0
    processed_ids = set()  # Track processed problem IDs to avoid duplicates

    # Process all problems looking for those with "graph" tag
    for i, raw_problem in enumerate(train_dataset):
        if successful >= target_problems:
            break

        # Convert to Pydantic model for better type safety
        try:
            dataset_problem = DatasetProblem.parse_obj(raw_problem)
        except ValidationError as e:
            logger.warning(f"Error parsing problem at index {i}: {e}")
            continue

        # Check if problem has "graph" tag
        if "graphs" not in dataset_problem.cf_tags:
            continue

        attempted += 1

        logger.info(
            f"Processing graph problem {attempted} (successful so far: {successful}): {dataset_problem.name}"
        )

        # Check if this problem might be a duplicate by name
        problem_id = get_problem_id(dataset_problem.name, i)
        if problem_id in processed_ids:
            logger.warning(
                f"Skipping potential duplicate problem: {dataset_problem.name}"
            )
            continue

        if process_problem(dataset_problem, i):
            successful += 1
            processed_ids.add(problem_id)

    logger.info(
        f"Finished processing. {successful}/{attempted} problems formatted successfully."
    )


if __name__ == "__main__":
    main()
