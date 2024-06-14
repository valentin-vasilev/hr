#!/usr/bin/env python


def main() -> None:
    """Main function"""
    s: str = input()
    sl: list = input().split()
    i: int = int(sl[0])
    c: str = sl[1]

    stl: list = list(s)
    stl[i] = c
    print("".join(stl))


if __name__ == "__main__":
    main()
