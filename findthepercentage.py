#!/usr/bin/env python


def main() -> None:
    """Main function"""
    n: int = int(input())
    if not 2 <= n <= 10:
        raise ValueError("n not in range")
    student_marks: dict = {}
    for _ in range(n):
        name, *line = input().split()
        if len(line) != 3:
            raise ValueError("line not in range")
        scores: list[float] = list(map(float, line))
        student_marks[name] = scores
    query_name: str = input()
    for name, scores in student_marks.items():
        if name == query_name:
            print(f"{sum(scores) / len(scores):.2f}")


if __name__ == "__main__":
    main()
