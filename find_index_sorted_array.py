"""Find index of item in sorted array"""


def finder(array: tuple, target: str, start: int, end: int) -> None:
    """Find index of target"""
    if start > end:
        print(f"Target: {target} not found")
    middle: int = (start + end) // 2
    if array[middle] == target:
        print(f"Target {target} found at index {middle}")
    if array[middle] > target:
        finder(array, target, start, middle - 1)
    if array[middle] < target:
        finder(array, target, middle + 1, end)


def main() -> None:
    """Main function"""
    series: tuple = tuple(input("Series: ").split(','))
    target: str = input("Target: ")
    finder(series, target, 0, len(series))


if __name__ == "__main__":
    main()
