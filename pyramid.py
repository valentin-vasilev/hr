#!/usr/bin/env python


def main() -> None:
    """Main function."""
    n: int = int(input())
    for i in range(1, n):
        print(i * (10**i - 1) // 9)


if __name__ == "__main__":
    main()
