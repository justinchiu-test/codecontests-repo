#!/usr/bin/env python3

from library import read_int, read_ints, binomial_mod, MOD

def solve():
    # Read input: n = total bloggers, k = bloggers to select
    n, k = read_ints()
    followers = read_ints()

    # Sort followers in descending order to pick bloggers with most followers
    followers.sort(reverse=True)

    # Count the frequency of each follower count
    frequency = {}
    for f in followers:
        frequency[f] = frequency.get(f, 0) + 1

    # Find the kth largest follower count (the threshold)
    threshold = followers[k-1]

    # Calculate how many bloggers have exactly the threshold followers
    total_with_threshold = frequency[threshold]

    # Calculate how many of those threshold bloggers we need to include
    # to reach exactly k bloggers
    needed_from_threshold = followers[:k].count(threshold)

    # The answer is the binomial coefficient: ways to choose needed_from_threshold
    # bloggers from total_with_threshold bloggers with the same follower count
    result = binomial_mod(total_with_threshold, needed_from_threshold, MOD)

    print(result)

def main():
    # Read number of test cases
    t = read_int()

    # Process each test case
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()