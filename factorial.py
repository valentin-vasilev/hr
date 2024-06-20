#!/usr/bin/env python


def factorial(n):
    """Calculate factorial of n"""
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main() -> None:
    """Main function"""
    n: int = int(input())
    print(factorial(n))


if __name__ == "__main__":
    main()
