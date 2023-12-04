"""Advent of Code 2023 day 3 solution."""
import numpy as np


def part1(test=False):
    """Returns answer to part 1 of the problem"""
    input_path = "input1"
    if test:
        input_path += ".test"
    with open(input_path, "r", encoding="utf-8") as F:
        lines = F.readlines()

    lines = [list(line[:-1]) for line in lines]  # -1 to ignore endline
    # we do a pass through the grid to label characters as adjacent to a symbol
    num_lines = len(lines)
    line_length = len(lines[0])
    adjacent = np.zeros((num_lines, line_length), dtype=np.uint8)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if not char.isnumeric() and char != ".":
                imin, imax = max(i - 1, 0), min(i + 1, line_length)
                jmin, jmax = max(j - 1, 0), min(j + 1, line_length)
                adjacent[imin : imax + 1, jmin : jmax + 1] = 1
                # clean up symbols for easy parsing later
                lines[i][j] = "."

    sum = 0
    # ok now do a pass looking for numbers that have an adjacent digit
    for i, line in enumerate(lines):
        number = ""
        found_adjacent = False
        for j, char in enumerate(line):
            if char.isnumeric():
                number += char
                if adjacent[i, j]:
                    found_adjacent = True
            else:
                if number and found_adjacent:
                    sum += int(number)
                number = ""
                found_adjacent = False
    if number and found_adjacent:
        sum += int(number)

    return sum


def part2(test=True):
    """Returns answer to part 2 of the problem"""
    input_path = "input2"
    if test:
        input_path += ".test"
    with open(input_path, "r", encoding="utf-8") as F:
        lines = F.readlines()

    lines = [list(line[:-1]) for line in lines]  # -1 to ignore endline
    # we do a pass through the grid to label characters as adjacent to a symbol
    num_lines = len(lines)
    line_length = len(lines[0])
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != "*":
                continue
            prod = 0
            # line above: scan 3 characters above
            if i > 0:
                
    return


def main():
    """Main function"""
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
