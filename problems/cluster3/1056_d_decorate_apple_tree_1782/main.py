#!/usr/bin/env python3

from library import read_int, read_tree, count_leaves

def main():
    n = read_int()
    # build tree from parent list for nodes 2..n
    adj = read_tree(n)
    # count leaves in each subtree
    leaves = count_leaves(adj, 0)
    # output sorted leaf counts
    leaves.sort()
    print(*leaves)

if __name__ == "__main__":
    main()
