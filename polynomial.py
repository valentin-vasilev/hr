#!/usr/bin/env python
#
# You are given a polynomial P of a single indeterminate (or variable), x.
# You are also given the values of x and k. Your task is to verify if P(x) = k.
#
# Constraints
# All coefficients of polynomial P are integers.
# x and y are also integers.
#
# Input Format
# The first line contains the space separated values of x and k
# The second line contains the polynomial P.
#
# Output Format
# Print True if P(x) = k. Otherwise, print False.


def eval_polynomial(p: str, x: int) -> int:
    """Evaluate polynomial"""
    return eval(p.replace("x", str(x)))


def main() -> None:
    """Main function"""
    x, k = map(int, input().split())
    p: str = input()
    if eval_polynomial(p, x) == k:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()
