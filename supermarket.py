#!/usr/bin/env python
# Task
#
# You are the manager of a supermarket.
# You have a list of  items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.
#
# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.
#
# Input Format
#
# The first line contains the number of items, .
# The next  lines contains the item's name and price, separated by a space.
#
# Constraints
# 0 < N <= 100

from collections import OrderedDict


def main() -> None:
    """Main function"""
    n: int = int(input())
    items: OrderedDict = OrderedDict()
    for _ in range(n):
        item, price = input().rsplit(maxsplit=1)
        items[item] = items.get(item, 0) + int(price)

    for item, price in items.items():
        print(item, price)


if __name__ == "__main__":
    main()
