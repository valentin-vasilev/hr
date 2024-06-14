#!/usr/bin/env python


def main() -> None:
    """Main function"""
    n, m = map(int, input().split())
    if 1 <= n <= 10**3 and 1 <= m <= 10**3:
        athletes: list[list[int]] = []
        for _ in range(n):
            attr: list[int] = list(map(int, input().split()))
            if len(attr) == m:
                athletes.append(attr)
            else:
                raise ValueError("m not in range")
        k = int(input())
        if 0 <= k < m:
            sorted_athletes: list[list[int]] = sorted(athletes, key=lambda x: x[k])
            for athlete in sorted_athletes:
                print(" ".join(map(str, athlete)))
        else:
            raise ValueError("n, m not in range")


if __name__ == "__main__":
    main()
