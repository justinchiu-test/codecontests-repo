#!/usr/bin/env python3
"""
Pre-commit hook to prevent edits to test files in problems/*/tests/
"""
import re
import sys

# Pattern to match test files
TEST_FILE_PATTERN = re.compile(r"problems/[^/]+/tests/.*")


def main():
    # Get modified files from pre-commit
    modified_files = []
    for line in sys.stdin:
        file_path = line.strip()
        if file_path:
            modified_files.append(file_path)

    # Check for test files
    test_files = [f for f in modified_files if TEST_FILE_PATTERN.match(f)]

    if test_files:
        print(
            "ERROR: Attempting to modify test files. These files should not be edited:"
        )
        for f in test_files:
            print(f"  - {f}")
        print("\nTest files are ground truth and should remain unmodified.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
