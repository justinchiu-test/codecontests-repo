# Parallel Claude Compression Script

## Overview
`claude_compression_parallel.sh` runs the code compression tasks with Claude in parallel across multiple clusters, significantly speeding up the process compared to the sequential version.

## Requirements
- GNU Parallel: Install with `brew install parallel` on macOS or `apt-get install parallel` on Ubuntu/Debian Linux
- Claude CLI: Must be properly configured
- Bash 4.0+ (standard on most modern systems)

## Usage
From the repository root directory:
```bash
./scripts/claude_compression_parallel.sh
```

By default, the script will:
1. Automatically detect available clusters in the `problems/` directory
2. Run up to 4 parallel processes (configurable in the script)
3. Generate results in the `results/` directory
4. Create a summary in `cluster_evaluation_summary.md`

## Customization
- To adjust the number of parallel jobs, modify the `NUM_JOBS` variable in the script
- To specify which clusters to process, edit the `CLUSTERS` array in the script

## Troubleshooting
If you encounter issues:
1. Ensure GNU Parallel is installed
2. Check Claude CLI is working correctly
3. Verify you have appropriate permissions to execute the script (`chmod +x scripts/claude_compression_parallel.sh`)
4. Run with bash verbosity for debugging: `bash -x scripts/claude_compression_parallel.sh`
