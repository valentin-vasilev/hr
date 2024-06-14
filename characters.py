#!/usr/bin/env python
# A newly opened multinational brand has decided to base their company logo
# on the three most common characters in the company name.
# They are now trying out various combinations of company names
# and logos based on this condition. Given a string s, which is the
# company name in lowercase letters, your task is to find the
# top three most common characters in the string.
#
# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical
# order.
# For example, according to the conditions described above,
#
# GOOGLE would have it's logo with the letters G,O,E.
#
# Input Format
#
# A single line of input containing the string s.
#
# Constraints
#
# 3 < len(s) < 10^4
# s has at least 3 distinct characters
import sys


def string_to_dict(s: str) -> dict:
    """Convert string to dictionary"""
    characters: dict = {}
    for char in s:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def validate_input(s: str) -> bool:
    """Validate input"""
    if isinstance(s, str) and 3 < len(s) <= 10**4:
        _characters = string_to_dict(s)
        if len(_characters) > 3:
            return True
    return False


def main() -> None:
    """Main function"""
    s: str = input()
    if not validate_input(s):
        sys.exit(1)
    characters: dict = string_to_dict(s)
    sorted_characters: dict = {
        char[0]: char[1]
        for char in sorted(characters.items(), key=lambda x: (-x[1], x[0]))
    }
    for item in list(sorted_characters.items())[:3]:
        print(item[0], item[1])


if __name__ == "__main__":
    main()
