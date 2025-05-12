#!/bin/bash

# This script automates the code compression task with Claude
# It loops through each cluster directory, runs Claude in that context

# Get the base directory
BASE_DIR=$(pwd)

# Loop through all cluster directories
for i in {0..9}; do
  CLUSTER_DIR="problems/cluster$i"

  # Check if this cluster directory exists
  if [ -d "$CLUSTER_DIR" ]; then
    echo "Processing $CLUSTER_DIR..."

    # Push into the cluster directory
    pushd "$CLUSTER_DIR" > /dev/null

    # Run Claude with instructions from base directory
    claude --dangerously-skip-permissions -p "Read the instructions in $BASE_DIR/INSTRUCTIONS.md. Be sure to read all the solutions to get an idea of what the library should look like. Then implement the library in $BASE_DIR/library/ while refactoring the solutions in the current directory. As you are refactoring solutions, run tests as described in INSTRUCTIONS.md to ensure they are correct. If tests fail, you are free to examine the inputs and outputs. Continue editing the library as you refactor solutions. Make sure solutions that use any changed library functions still pass."

    # Pop back to the original directory
    popd > /dev/null

    echo "Completed $CLUSTER_DIR"
  else
    echo "Skipping $CLUSTER_DIR - directory does not exist"
  fi
done

echo "All clusters processed!"
