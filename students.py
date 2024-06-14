#!/usr/bin/env python


def main() -> None:
    """Main function"""
    n: int = int(input())
    records: list[list] = []
    for _ in range(n):
        name: str = input()
        score: float = float(input())
        records.append([name, score])

    sorted_records: list[list] = sorted(records, key=lambda x: x[1])
    for i in range(len(sorted_records)):
        if sorted_records[i + 1][1] != sorted_records[i][1]:
            second_lowest: float = sorted_records[i + 1][1]
            break
    second_lowest_records: list[list] = [
        [x[0], x[1]]
        for x in sorted(sorted_records, key=lambda y: y[0])
        if x[1] == second_lowest
    ]
    for record in second_lowest_records:
        print(record[0])


if __name__ == "__main__":
    main()
