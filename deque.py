#!/usr/bin/env python
# Task
#
# Perform append, pop, popleft and appendleft methods on an empty deque .
#
# Input Format
#
# The first line contains an integer , the number of operations.
# The next  lines contains the space separated names of methods
# and their values.
#
# Constraints
# 0 < N <= 100
#
# Output Format
#
# Print the space separated elements of deque .

from collections import deque


def main() -> None:
    """Main function"""
    n: int = int(input())
    d: deque = deque()

    for _ in range(n):
        parts = input().split()

        if len(parts) == 1:
            command = parts[0]
            getattr(d, command)()
        else:
            command, value = parts
            getattr(d, command)(value)

    print(*d)


if __name__ == "__main__":
    main()
