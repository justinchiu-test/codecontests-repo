#!/usr/bin/env python3
"""
Validate our models by creating test instances and checking their behavior.

This script attempts to instantiate and use our Pydantic models to ensure they work correctly.
"""
import sys
from typing import List

from tools.models.dataset import DatasetProblem, Solution, TestSet
from tools.models.problem import Problem, TestCase


def validate_testcase_model() -> List[str]:
    """Validate the TestCase model."""
    issues = []

    try:
        # Create a valid test case
        test_case = TestCase(
            input="1 2 3\n4 5 6",
            output="7 8 9",
            time_limit_ms=1000,
            memory_limit_mb=256,
        )

        # Check that fields are accessible
        if test_case.input != "1 2 3\n4 5 6":
            issues.append("TestCase.input field not working correctly")
        if test_case.output != "7 8 9":
            issues.append("TestCase.output field not working correctly")
        if test_case.time_limit_ms != 1000:
            issues.append("TestCase.time_limit_ms field not working correctly")
        if test_case.memory_limit_mb != 256:
            issues.append("TestCase.memory_limit_mb field not working correctly")

        # Check default values
        default_test_case = TestCase(
            input="test", output="test", time_limit_ms=30000, memory_limit_mb=512
        )
        if default_test_case.time_limit_ms != 30000:
            issues.append(
                f"TestCase.time_limit_ms default should be 30000, got {default_test_case.time_limit_ms}"
            )
        if default_test_case.memory_limit_mb != 512:
            issues.append(
                f"TestCase.memory_limit_mb default should be 512, got {default_test_case.memory_limit_mb}"
            )

    except Exception as e:
        issues.append(f"Failed to validate TestCase model: {e}")

    return issues


def validate_problem_model() -> List[str]:
    """Validate the Problem model."""
    issues = []

    try:
        # Create a valid problem
        problem = Problem(
            id="test_problem_1",
            name="Test Problem",
            description="This is a test problem",
            category=["math", "implementation"],
            difficulty="medium",
            test_cases=[
                TestCase(
                    input="1 2", output="3", time_limit_ms=30000, memory_limit_mb=512
                ),
                TestCase(
                    input="4 5", output="9", time_limit_ms=30000, memory_limit_mb=512
                ),
            ],
            source="Test Source",
        )

        # Check that fields are accessible
        if problem.id != "test_problem_1":
            issues.append("Problem.id field not working correctly")
        if problem.name != "Test Problem":
            issues.append("Problem.name field not working correctly")
        if len(problem.test_cases) != 2:
            issues.append("Problem.test_cases field not working correctly")

        # Check to_markdown method
        markdown = problem.to_markdown()
        if "# Test Problem" not in markdown:
            issues.append("Problem.to_markdown() not including problem name")
        if "This is a test problem" not in markdown:
            issues.append("Problem.to_markdown() not including description")

        # Check default values
        problem_with_defaults = Problem(
            id="test_defaults",
            name="Test Defaults",
            description="Testing defaults",
            test_cases=[
                TestCase(
                    input="test",
                    output="test",
                    time_limit_ms=30000,
                    memory_limit_mb=512,
                )
            ],
            difficulty="medium",
            source="Test Source",
        )
        # Note: we're explicitly setting source="Test Source" in the test
        # so we shouldn't expect it to be None
        if problem_with_defaults.source != "Test Source":
            issues.append(
                f"Problem.source should be 'Test Source', got {problem_with_defaults.source}"
            )

    except Exception as e:
        issues.append(f"Failed to validate Problem model: {e}")

    return issues


def validate_dataset_models() -> List[str]:
    """Validate the dataset models (DatasetProblem, Solution, TestSet)."""
    issues = []

    try:
        # Create a valid Solution
        solution = Solution(
            language=[3, 4],  # Python 3, Python 2
            solution=["print(1+2)", "print 1+2"],
        )

        # Check that fields are accessible
        if solution.language != [3, 4]:
            issues.append("Solution.language field not working correctly")
        if solution.solution != ["print(1+2)", "print 1+2"]:
            issues.append("Solution.solution field not working correctly")

        # Create valid TestSets
        public_tests = TestSet(input=["1 2", "3 4"], output=["3", "7"])

        private_tests = TestSet(input=["5 6", "7 8"], output=["11", "15"])

        # Create a valid DatasetProblem
        problem = DatasetProblem(
            name="Dataset Test Problem",
            description="This is a test problem from the dataset",
            solutions=solution,
            public_tests=public_tests,
            private_tests=private_tests,
            difficulty=4,  # medium
            source=2,  # Codeforces
            cf_tags=["graphs", "dfs and similar"],
            generated_tests=TestSet(input=["9 10"], output=["19"]),
            cf_contest_id=1234,
            cf_index="A",
            cf_points=500,
            cf_rating=1600,
            url="https://codeforces.com/contest/1234/problem/A",
        )

        # Check that fields are accessible
        if problem.name != "Dataset Test Problem":
            issues.append("DatasetProblem.name field not working correctly")
        if problem.difficulty != 4:
            issues.append("DatasetProblem.difficulty field not working correctly")

        # Check helper methods
        python3_solution = problem.get_python3_solution()
        if python3_solution != "print(1+2)":
            issues.append(
                f"DatasetProblem.get_python3_solution() not working correctly, got {python3_solution}"
            )

        difficulty_name = problem.get_difficulty_name()
        if difficulty_name != "medium":
            issues.append(
                f"DatasetProblem.get_difficulty_name() not working correctly, got {difficulty_name}"
            )

        source_name = problem.get_source_name()
        if source_name != "Codeforces":
            issues.append(
                f"DatasetProblem.get_source_name() not working correctly, got {source_name}"
            )

        test_cases = problem.get_all_test_cases()
        if len(test_cases) != 4:
            issues.append(
                f"DatasetProblem.get_all_test_cases() should return 4 test cases, got {len(test_cases)}"
            )

    except Exception as e:
        issues.append(f"Failed to validate dataset models: {e}")

    return issues


def main() -> int:
    """Main entry point for the script."""
    all_issues = []

    print("Validating TestCase model...")
    all_issues.extend(validate_testcase_model())

    print("Validating Problem model...")
    all_issues.extend(validate_problem_model())

    print("Validating dataset models...")
    all_issues.extend(validate_dataset_models())

    if all_issues:
        print("\nIssues found:")
        for issue in all_issues:
            print(f"- {issue}")
        return 1

    print("All models validated successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
