#!/bin/bash

# This script evaluates the pass rates of all clusters without running Claude
# It can be used to generate a report on the current state of the solutions

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

    # Return the pass rate for summary
    local pass_rate=$(echo "scale=2; 100*$passed_problems/$total_problems" | bc)
    echo "$passed_problems|$total_problems|$pass_rate"
}

# Create a summary file with results from all clusters
echo "# Cluster Evaluation Summary" > "$BASE_DIR/cluster_evaluation_summary.md"
echo "Generated on: $(date)" >> "$BASE_DIR/cluster_evaluation_summary.md"
echo "" >> "$BASE_DIR/cluster_evaluation_summary.md"
echo "| Cluster | Problems Passed | Total Problems | Pass Rate |" >> "$BASE_DIR/cluster_evaluation_summary.md"
echo "|---------|----------------|----------------|-----------|" >> "$BASE_DIR/cluster_evaluation_summary.md"

# Loop through all cluster directories
for i in {0..9}; do
  CLUSTER_DIR="problems/cluster$i"

  # Check if this cluster directory exists
  if [ -d "$CLUSTER_DIR" ]; then
    echo "Processing $CLUSTER_DIR..."

    # Evaluate pass rates for this cluster
    RESULT=$(evaluate_cluster $i)
    PASS_INFO=$(echo "$RESULT" | tail -n 1)

    # Extract information for summary table
    PASSED=$(echo "$PASS_INFO" | cut -d '|' -f1)
    TOTAL=$(echo "$PASS_INFO" | cut -d '|' -f2)
    RATE=$(echo "$PASS_INFO" | cut -d '|' -f3)

    echo "| Cluster $i | $PASSED | $TOTAL | ${RATE}% |" >> "$BASE_DIR/cluster_evaluation_summary.md"

    echo "Completed $CLUSTER_DIR"
  else
    echo "Skipping $CLUSTER_DIR - directory does not exist"
  fi
done

echo "All clusters evaluated! Results available in cluster_evaluation_summary.md"
