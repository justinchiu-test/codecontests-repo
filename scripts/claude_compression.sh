#!/bin/bash

# This script automates the code compression task with Claude
# It reads instructions, makes a plan, and implements the plan

claude --dangerously-skip-permissions -p "Read the instructions in INSTRUCTIONS.md. Be sure to read all the solutions to get an idea of what the library should look like. Then implement the library in `library/` while refactoring the solutions in `problems/` do this for all problems in `problems/*`. As you are refactoring solutions, run tests as described in INSTRUCTIONS.md to ensure they are correct. If tests fail, you are free to examine the inputs and outputs. Continue editing `library` as you refactor solutions. Make sure solutions that use any changed library functions still pass."
