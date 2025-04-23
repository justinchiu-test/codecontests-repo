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
from typing import Any, Dict, List, Optional

from datasets import load_dataset

from tools.formatter.problem_md import generate_problem_md
from tools.formatter.script_sh import generate_run_script

# Import the models correctly using absolute imports
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


def extract_python_solution(problem: Dict[str, Any]) -> Optional[str]:
    """
    Extract a Python 3 solution from the problem's solutions.
    Only returns Python 3 solutions, skipping Python 2 solutions.

    Args:
        problem: Problem dictionary from the dataset

    Returns:
        Python 3 solution code or None if not found
    """
    # The dataset structure has 'solutions' as a dict with 'language' and 'solution' lists
    solutions_dict = problem.get("solutions", {})

    if not isinstance(solutions_dict, dict):
        logger.warning(f"Solutions is not a dictionary: {type(solutions_dict)}")
        return None

    languages = solutions_dict.get("language", [])
    solution_codes = solutions_dict.get("solution", [])

    # Find Python 3 solutions only (language code 3 is Python 3)
    python3_solutions = []
    for i, lang in enumerate(languages):
        if lang == 3 and i < len(solution_codes):  # 3 is the code for Python 3
            python3_solutions.append(solution_codes[i])

    if python3_solutions:
        logger.info(f"Found Python 3 solution for problem: {problem.get('name')}")
        return python3_solutions[0]  # Return the first Python 3 solution

    # If no Python 3 solution, skip this problem
    logger.warning(
        f"No Python 3 solution found for problem: {problem.get('name')}, skipping"
    )
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


def process_problem(problem: Dict[str, Any], index: int) -> bool:
    """
    Process a single problem and create its directory structure.

    Args:
        problem: Problem dictionary from the dataset
        index: Problem index for unique ID generation

    Returns:
        True if processing succeeded, False otherwise
    """
    try:
        name = problem.get("name", f"Unknown_{index}")
        problem_id = get_problem_id(name, index)

        # Create problem directory
        problem_dir = PROBLEMS_DIR / problem_id
        problem_dir.mkdir(parents=True, exist_ok=True)

        # Extract Python solution
        solution_code = extract_python_solution(problem)
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

        # Collect test cases from public, private, and generated tests
        all_inputs = []
        all_outputs = []

        # Add public tests
        public_tests = problem.get("public_tests", {})
        if isinstance(public_tests, dict):
            all_inputs.extend(public_tests.get("input", []))
            all_outputs.extend(public_tests.get("output", []))

        # Add private tests if available
        private_tests = problem.get("private_tests", {})
        if isinstance(private_tests, dict):
            all_inputs.extend(private_tests.get("input", []))
            all_outputs.extend(private_tests.get("output", []))

        # Add generated tests if available and if we need more tests
        if len(all_inputs) < 3:
            generated_tests = problem.get("generated_tests", {})
            if isinstance(generated_tests, dict):
                gen_inputs = generated_tests.get("input", [])
                gen_outputs = generated_tests.get("output", [])
                if len(gen_inputs) == len(gen_outputs):
                    all_inputs.extend(gen_inputs)
                    all_outputs.extend(gen_outputs)

        # Make sure we have the same number of inputs and outputs
        min_count = min(len(all_inputs), len(all_outputs))
        all_inputs = all_inputs[:min_count]
        all_outputs = all_outputs[:min_count]

        # Skip if no test cases
        if not all_inputs:
            logger.warning(f"Skipping problem {name} due to missing test cases")
            return False

        # Create test cases for the problem model
        test_cases = [
            TestCase(input=inp, output=out) for inp, out in zip(all_inputs, all_outputs)
        ]

        # Get difficulty as string
        difficulty_level = problem.get("difficulty")
        if isinstance(difficulty_level, int):
            difficulty_str = {
                1: "very easy",
                2: "easy",
                3: "easy-medium",
                4: "medium",
                5: "medium-hard",
                6: "hard",
                7: "very hard",
            }.get(difficulty_level, str(difficulty_level))
        else:
            difficulty_str = str(difficulty_level) if difficulty_level else "Unknown"

        # Get source
        source_id = problem.get("source")
        source_name = (
            {
                1: "CodeChef",
                2: "Codeforces",
                3: "AtCoder",
                4: "HackerEarth",
                5: "Aizu",
            }.get(source_id, "Unknown")
            if isinstance(source_id, int)
            else "Unknown"
        )

        # Get tags/categories
        tags = problem.get("cf_tags", [])

        problem_model = Problem(
            id=problem_id,
            name=name,
            description=problem.get("description", "No description available"),
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
    train_problems = dataset["train"]

    # Set target for graph problems
    target_problems = 100  # Target number of graph problems to process

    logger.info("Searching for graph problems with Python 3 solutions")
    logger.info(f"Target: {target_problems} graph problems with Python 3 solutions")

    successful = 0
    attempted = 0
    processed_ids = set()  # Track processed problem IDs to avoid duplicates

    # Process all problems looking for those with "graph" tag
    for i in range(len(train_problems)):
        if successful >= target_problems:
            break

        problem = train_problems[i]

        # Check if problem has "graph" tag
        tags = problem.get("cf_tags", [])
        if "graphs" not in tags:
            continue

        attempted += 1

        problem_name = problem.get("name", "Unknown")
        logger.info(
            f"Processing graph problem {attempted} (successful so far: {successful}): {problem_name}"
        )

        # Check if this problem might be a duplicate by name
        problem_id = get_problem_id(problem_name, i)
        if problem_id in processed_ids:
            logger.warning(f"Skipping potential duplicate problem: {problem_name}")
            continue

        if process_problem(problem, i):
            successful += 1
            processed_ids.add(problem_id)

    logger.info(
        f"Finished processing. {successful}/{attempted} problems formatted successfully."
    )


if __name__ == "__main__":
    main()
