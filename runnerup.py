#!/usr/bin/env python
# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given n scores.
# Store them in a list and find the score of the runner-up.
#
# Input Format
#
# The first line contains n. The second line contains an array
# a[i] of n integers each separated by a space.
#
# Constraints
# 2 <= n <= 10
# -100 <= a[i] <= 100


def main() -> None:
    """Main function"""
    n: int = int(input())
    if not 2 <= n <= 10:
        raise ValueError("n not in range")
    a: list[int] = list(map(int, input().split()))
    if len(a) != n:
        raise ValueError("a not in range")
    for _ in a:
        if not -100 <= _ <= 100:
            raise ValueError("a[i] not in range")
    for score in sorted(a, reverse=True):
        if score < max(a):
            print(score)
            break


if __name__ == "__main__":
    main()
