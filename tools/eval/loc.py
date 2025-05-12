"""
Tools for counting logical lines of code (LLOC) in Python files.

This module provides utilities to measure the amount of actual code in files,
excluding comments, docstrings, and blank lines. This gives a more accurate
measure of code complexity than raw line counts.
"""

import ast
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Union


def count_lloc(file_path: Union[str, Path]) -> int:
    """
    Count logical lines of code in a Python file.

    Args:
        file_path: Path to the Python file

    Returns:
        Number of logical lines of code (excluding comments, docstrings, blank lines)
    """
    file_path = Path(file_path)
    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not str(file_path).endswith(".py"):
        raise ValueError(f"Not a Python file: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        # Parse the AST
        tree = ast.parse(source)

        # Count the number of AST nodes that represent statements
        lloc_counter = LlocCounter()
        lloc_counter.visit(tree)

        return lloc_counter.lloc
    except SyntaxError:
        # Fall back to a simpler approach for files with syntax errors
        return count_lloc_simple(source)


def count_lloc_simple(source: str) -> int:
    """
    Count logical lines of code using a simpler approach.

    This is used as a fallback when AST parsing fails.

    Args:
        source: Python source code

    Returns:
        Approximate number of logical lines of code
    """
    # Remove multiline string literals (potential docstrings)
    pattern = r'""".*?"""|\'\'\'.*?\'\'\''
    source = re.sub(pattern, "", source, flags=re.DOTALL)

    # Remove single-line comments
    source = re.sub(r"#.*$", "", source, flags=re.MULTILINE)

    # Remove blank lines
    lines = [line.strip() for line in source.split("\n")]
    non_empty_lines = [line for line in lines if line]

    # Count non-empty, non-comment lines
    return len(non_empty_lines)


class LlocCounter(ast.NodeVisitor):
    """
    AST visitor that counts logical lines of code.
    """

    def __init__(self):
        self.lloc = 0

    def visit(self, node):
        # Count most statement nodes
        if isinstance(
            node,
            (
                ast.Assign,
                ast.AnnAssign,
                ast.AugAssign,
                ast.Return,
                ast.Delete,
                ast.Raise,
                ast.Assert,
                ast.Import,
                ast.ImportFrom,
                ast.Global,
                ast.Nonlocal,
                ast.Pass,
                ast.Break,
                ast.Continue,
            ),
        ):
            self.lloc += 1

        # Count control flow statements
        elif isinstance(node, (ast.If, ast.For, ast.While, ast.With)):
            self.lloc += 1

        # Count function and class definitions
        elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            self.lloc += 1

        # Count expressions that are statements
        elif isinstance(node, ast.Expr):
            # Skip docstrings (string literals at the module/class/function level)
            if not (isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)):
                self.lloc += 1

        # Count each clause in try/except blocks separately
        elif isinstance(node, ast.Try):
            self.lloc += 1  # Count the try part
            self.lloc += len(node.handlers)  # Count each except clause
            if node.finalbody:
                self.lloc += 1  # Count the finally clause
            if node.orelse:
                self.lloc += 1  # Count the else clause

        # Count comprehensions
        elif isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            self.lloc += 1

        # Recursively visit all child nodes
        super().generic_visit(node)


def count_lloc_directory(
    directory: Union[str, Path],
    exclude_dirs: Optional[Set[str]] = None,
    include_patterns: Optional[List[str]] = None,
) -> Dict[str, int]:
    """
    Count logical lines of code in all Python files in a directory.

    Args:
        directory: Path to the directory
        exclude_dirs: Set of directory names to exclude
        include_patterns: List of glob patterns to include (e.g., ["**/*.py"])

    Returns:
        Dictionary mapping file paths to LLOC counts
    """
    directory = Path(directory)
    if not directory.exists() or not directory.is_dir():
        raise FileNotFoundError(f"Directory not found: {directory}")

    exclude_dirs = exclude_dirs or {"__pycache__", ".git", ".venv", "venv", "env"}
    include_patterns = include_patterns or ["**/*.py"]

    lloc_counts = {}

    # Process all files matching the include patterns
    for pattern in include_patterns:
        for file_path in directory.glob(pattern):
            # Skip directories in the exclude list
            if any(exclude_dir in file_path.parts for exclude_dir in exclude_dirs):
                continue

            try:
                lloc = count_lloc(file_path)
                lloc_counts[str(file_path.relative_to(directory))] = lloc
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    return lloc_counts


def summarize_lloc(
    lloc_counts: Dict[str, int], group_by_directory: bool = True
) -> Dict[str, Union[int, Dict[str, int]]]:
    """
    Summarize LLOC counts, optionally grouping by directory.

    Args:
        lloc_counts: Dictionary mapping file paths to LLOC counts
        group_by_directory: Whether to group results by directory

    Returns:
        Dictionary with summary statistics
    """
    summary: Dict[str, Union[int, Dict[str, int]]] = {
        "total_lloc": sum(lloc_counts.values()),
        "file_count": len(lloc_counts),
    }

    if group_by_directory:
        directories: Dict[str, int] = {}
        for file_path, lloc in lloc_counts.items():
            directory = os.path.dirname(file_path) or "."
            directories.setdefault(directory, 0)
            directories[directory] += lloc

        summary["directories"] = directories

    return summary


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) < 2:
        print("Usage: python loc.py <directory> [--json]")
        sys.exit(1)

    directory = sys.argv[1]
    output_json = "--json" in sys.argv

    try:
        lloc_counts = count_lloc_directory(directory)
        summary = summarize_lloc(lloc_counts)

        if output_json:
            print(json.dumps(summary, indent=2))
        else:
            print(f"Total LLOC: {summary['total_lloc']}")
            print(f"Files processed: {summary['file_count']}")
            print("\nDirectory breakdown:")
            directories = summary.get("directories", {})
            if isinstance(directories, dict):
                for dir_name, lloc in sorted(directories.items()):
                    print(f"  {dir_name}: {lloc}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
