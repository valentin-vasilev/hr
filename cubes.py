#!/usr/bin/env python
# There is a horizontal row of n cubes. The length of each cube is given.
# You need to create a new vertical pile of cubes.
# The new pile should follow these directions: if cube[i] is on top of cube[j]
# sideLength[j] >= sideLength[i] then.
#
# When stacking the cubes, you can only pick up either the leftmost
# or the rightmost cube each time. Print Yes if it is possible to
# stack the cubes. Otherwise, print No.
#
# Example
# blocks = [1, 2, 3, 8, 7]
# Result: No
#
# After choosing the rightmost element, , choose the leftmost element, .
# After than, the choices are  and .
# These are both larger than the top block of size .
#
# blocks = [1, 2, 3, 7, 8]
# Result: Yes
#
# Choose blocks from right to left in order to successfully stack the blocks.
#
# Input Format
#
# The first line contains a single integer T, the number of test cases.
# For each test case, there are  lines.
# The first line of each test case contains n, the number of cubes.
# The second line contains  space separated integers,
# denoting the sideLengths of each cube in that order.
#
# Constraints
#
# 1 <= T <= 5
# 1 <= n <= 10^5
# 1 <= sideLength <= 2^31
#


def main() -> None:
    """Main function"""
    while True:
        t: int = int(input("Enter test cases: "))
        if t < 1 or t > 5:
            print("Invalid test cases should be between 1 and 5 inclusive.")
            continue
        break
    for _ in range(t):
        while True:
            n: int = int(input(f"Enter number of cubes {_+1}: "))
            if n < 1 or n > 10**5:
                print("Invalid number of cubes should be between 1 and 10^5.")
                continue
            while True:
                side_lengths: list[int] = list(
                    map(int, input(f"Enter side lengths {_+1}: ").split())
                )
                if len(side_lengths) != n:
                    print("Invalid side lengths.")
                    continue
                answer: str = "Yes"
                for i in range(1, len(side_lengths) - 1):
                    if (
                        side_lengths[i] > side_lengths[i - 1]
                        and side_lengths[i] > side_lengths[i + 1]
                    ):
                        answer = "No"
                        break
                print(answer)
                break
            break


if __name__ == "__main__":
    main()
