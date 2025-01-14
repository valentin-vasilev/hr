"""Find index of a target in unsorted array"""


def finder(series: tuple, target: str, start: int, end: int) -> None:
    """Finder in unsorted array with front and back index"""
    if start > end:
        print(f"Target {target} not found")
    elif series[start] == target:
        print(f"Found {target} at index {start}")
    elif series[end] == target:
        print(f"Found {target} at index {end}")
    else:
        finder(series, target, start + 1, end - 1)


def main() -> None:
    """Main function"""
    series: tuple = tuple(input("Series: ").split(","))
    target: str = input("Target: ")
    finder(series, target, 0, len(series) - 1)

if __name__ == "__main__":
    main()
