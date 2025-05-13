#!/bin/bash

# This script automates the code compression task with Claude
# It loops through each cluster directory, runs Claude in that context,
# and evaluates the pass rates of the problems in each cluster

# Get the base directory
BASE_DIR=$(pwd)

# Function to evaluate cluster pass rates
evaluate_cluster() {
    local cluster_num=$1
    local cluster_dir="problems/cluster$cluster_num"

    echo "Evaluating test pass rates for $cluster_dir..."

    # Variables to track pass rates
    local total_problems=0
    local passed_problems=0
    local problem_results=()

    # Process each problem directory
    for problem_dir in "$cluster_dir"/*; do
        # Skip if it's not a directory or if it's the library.py file
        if [ ! -d "$problem_dir" ] || [ "$(basename "$problem_dir")" = "library.py" ]; then
            continue
        fi

        local problem_name=$(basename "$problem_dir")

        # Check if run.sh exists
        if [ ! -f "$problem_dir/run.sh" ]; then
            echo "  - Skipping $problem_name: run.sh not found"
            continue
        fi

        echo "  - Testing $problem_name..."

        # Run the test script
        pushd "$problem_dir" > /dev/null
        TEST_OUTPUT=$(./run.sh 2>&1)
        TEST_RESULT=$?
        popd > /dev/null

        # Extract pass/fail information
        local results_line=$(echo "$TEST_OUTPUT" | grep -E "Results: [0-9]+/[0-9]+ tests passed" || echo "Results: unknown")
        local passed_test_count=$(echo "$results_line" | sed -E 's/Results: ([0-9]+)\/([0-9]+) tests passed/\1/' || echo "unknown")
        local total_test_count=$(echo "$results_line" | sed -E 's/Results: ([0-9]+)\/([0-9]+) tests passed/\2/' || echo "unknown")

        total_problems=$((total_problems+1))
        if [ $TEST_RESULT -eq 0 ]; then
            passed_problems=$((passed_problems+1))
            echo "    ✅ All tests passed ($results_line)"
            problem_results+=("$problem_name: PASS - $results_line")
        else
            echo "    ❌ Some tests failed ($results_line)"
            problem_results+=("$problem_name: FAIL - $results_line")
        fi
    done

    # Print summary
    echo
    echo "==========================================="
    echo "CLUSTER $cluster_num EVALUATION SUMMARY"
    echo "==========================================="
    echo "Problems passed: $passed_problems/$total_problems ($(echo "scale=2; 100*$passed_problems/$total_problems" | bc)%)"
    echo
    echo "Problem details:"
    for result in "${problem_results[@]}"; do
        echo "  - $result"
    done
    echo "==========================================="
    echo

    # Save results to file
    echo "Cluster $cluster_num evaluation: $passed_problems/$total_problems problems passed" > "$BASE_DIR/problems/cluster$cluster_num/evaluation_results.txt"
    echo "Pass rate: $(echo "scale=2; 100*$passed_problems/$total_problems" | bc)%" >> "$BASE_DIR/problems/cluster$cluster_num/evaluation_results.txt"
    echo >> "$BASE_DIR/problems/cluster$cluster_num/evaluation_results.txt"
    echo "Problem details:" >> "$BASE_DIR/problems/cluster$cluster_num/evaluation_results.txt"
    for result in "${problem_results[@]}"; do
        echo "  - $result" >> "$BASE_DIR/problems/cluster$cluster_num/evaluation_results.txt"
    done
}

mkdir -p results

# Loop through all cluster directories
#for i in {0..3}; do
for i in {4..7}; do
  CLUSTER_DIR="problems/cluster$i"

  # Check if this cluster directory exists
  if [ -d "$CLUSTER_DIR" ]; then
    echo "Processing $CLUSTER_DIR..."

    # Push into the cluster directory
    pushd "$CLUSTER_DIR" > /dev/null

    # Run Claude with instructions from cluster directory
    codex --approval-mode full-auto "Read the instructions in $BASE_DIR/INSTRUCTIONS.md. Be sure to read all the solutions to get an idea of what the library should look like. Then make a plan for the library in PLAN.md. Then implement the library in library.py while refactoring the solutions in the current directory. As you are refactoring solutions, run tests as described in INSTRUCTIONS.md to ensure they are correct. If tests fail, you are free to examine the inputs and outputs. Continue editing the library as you refactor solutions. Make sure solutions that use any changed library functions still pass. Your goal is to make the library and solutions as compact as possible."
    # Twice for laziness
    codex --approval-mode full-auto "Read the instructions in $BASE_DIR/INSTRUCTIONS.md. Be sure to read all the solutions to get an idea of what the library should look like. Read your plan in PLAN.md. Finish implementing the library in library.py while continuing to refactor the solutions in the current directory. As you are refactoring solutions, run tests as described in INSTRUCTIONS.md to ensure they are correct. If tests fail, you are free to examine the inputs and outputs. Continue editing the library as you refactor solutions. Make sure solutions that use any changed library functions still pass. Your goal is to make the library and solutions as compact as possible."


    # Pop back to the original directory
    popd > /dev/null

    # Evaluate pass rates after Claude processing
    evaluate_cluster $i > results/cluster_${i}_results.txt

    echo "Completed $CLUSTER_DIR"
  else
    echo "Skipping $CLUSTER_DIR - directory does not exist"
  fi
done

# Create a summary file with results from all clusters
echo "# Cluster Evaluation Summary" > "$BASE_DIR/cluster_evaluation_summary.md"
echo "Generated on: $(date)" >> "$BASE_DIR/cluster_evaluation_summary.md"
echo "" >> "$BASE_DIR/cluster_evaluation_summary.md"
echo "| Cluster | Problems Passed | Total Problems | Pass Rate |" >> "$BASE_DIR/cluster_evaluation_summary.md"
echo "|---------|----------------|----------------|-----------|" >> "$BASE_DIR/cluster_evaluation_summary.md"

for i in {0..9}; do
  CLUSTER_DIR="problems/cluster$i"
  if [ -d "$CLUSTER_DIR" ] && [ -f "$CLUSTER_DIR/evaluation_results.txt" ]; then
    PASS_INFO=$(head -n 1 "$CLUSTER_DIR/evaluation_results.txt" | sed -E 's/Cluster [0-9]+ evaluation: ([0-9]+)\/([0-9]+) problems passed/\1|\2/')
    PASS_RATE=$(head -n 2 "$CLUSTER_DIR/evaluation_results.txt" | tail -n 1 | sed -E 's/Pass rate: ([0-9.]+)%/\1%/')
    echo "| Cluster $i | ${PASS_INFO} | ${PASS_RATE} |" >> "$BASE_DIR/cluster_evaluation_summary.md"
  fi
done

echo "All clusters processed! Summary available in cluster_evaluation_summary.md"
