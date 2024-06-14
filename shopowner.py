#!/usr/bin/env python


def main() -> None:
    """Main function"""
    x: int = int(input())
    if not 1 <= x <= 10**3:
        raise ValueError("x not in range")
    size_list: list[int] = list(map(int, input().split()))
    for size in size_list:
        if not 2 <= size <= 20:
            raise ValueError("size not in range")
    n: int = int(input())
    customer_desired: list[int] = []
    for _ in range(n):
        size, price = map(int, input().split())
        if not 2 <= size <= 20 and 20 <= price <= 10**2:
            raise ValueError("size, price not in range")
        customer_desired.append(size)
        customer_desired.append(price)
    print(customer_desired)


if __name__ == "__main__":
    main()
