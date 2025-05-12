#!/usr/bin/env python3
"""
Script to load the codecontests dataset and cluster JSONL files.

This script:
1. Loads problems from the deepmind/code_contests dataset
2. Loads problems from each cluster in path_to_clusters/*.jsonl
3. Analyzes the overlap between dataset problems and cluster problems
"""

import json
import logging
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List

from datasets import load_dataset

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Constants
DATASET_NAME = "deepmind/code_contests"
REPO_ROOT = Path(__file__).resolve().parents[1]
CLUSTERS_DIR = REPO_ROOT / "data" / "clusters"


def load_cluster_problems() -> Dict[str, List[Dict[str, Any]]]:
    """
    Load problems from all cluster JSONL files.

    Returns:
        Dictionary mapping cluster IDs to lists of problem data
    """
    clusters = {}

    for cluster_file in sorted(CLUSTERS_DIR.glob("*.jsonl")):
        cluster_id = cluster_file.stem
        problems = []

        with open(cluster_file, "r") as f:
            for line in f:
                problem_data = json.loads(line.strip())
                problems.append(problem_data)

        clusters[cluster_id] = problems
        logger.info(f"Loaded {len(problems)} problems from cluster {cluster_id}")

    return clusters


def main():
    """Main entry point for the script."""
    # Load cluster problems
    cluster_problems = load_cluster_problems()

    # Load dataset problems
    dataset = load_dataset(DATASET_NAME, split="train")
    names = set([x["name"] for x in dataset])

    clusters = defaultdict(list)
    for id, cluster in cluster_problems.items():
        for problem in cluster:
            assert problem["name"] in names
            clusters[id].append(problem["name"])

    # Save matching information to a file
    output_file = REPO_ROOT / "data" / "clusters.json"
    with open(output_file, "w") as f:
        json.dump(clusters, f, indent=2)


if __name__ == "__main__":
    main()
