#!/bin/bash

# This script automates the code compression task with Claude
# It reads instructions, makes a plan, and implements the plan

claude --dangerously-skip-permissions -p "read the instructions in INSTRUCTIONS.md. then implement the library in `library/` while refactoring the solutions in `problems/` do this for all problems in `problems/*`. as you are refactoring solutions, run tests as described in INSTRUCTIONS.md to ensure they are correct. if tests fail, you are free to examine the inputs and outputs."
