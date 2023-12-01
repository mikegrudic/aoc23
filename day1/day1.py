"""Advent of Code 2023 Day 1 Problem"""


def part1():
    """Returns the answer for Part 1"""
    lines = open("input1", encoding="utf-8").readlines()
    return sum(line_number(l) for l in lines)


def part2():
    """Returns the answer for Part 2"""
    lines = open("input1b", encoding="utf-8").readlines()
    return sum(line_number(l, part=2) for l in lines)


def line_number(line: str, part=1) -> int:
    """Returns the number made from the first
    and last digit in each line of s"""
    line_old = line
    if part == 2:
        replacements = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        possible_digits = list(replacements.keys()) + list(replacements.values())
        first = last = None
        pos = 0
        while pos < len(line) + 1:
            if first:
                break
            pos += 1
            for d in possible_digits:
                if d in line[:pos]:
                    first = d
                    if d in replacements:
                        first = replacements[d]
                    break
        pos = len(line) + 1
        while pos > 0:
            if last:
                break
            pos -= 1
            for d in possible_digits:
                if d in line[pos:]:
                    last = d
                    if d in replacements:
                        last = replacements[d]
                    break
        return int(first + last)

    digits = list(filter(str.isnumeric, line))
    return int(digits[0] + digits[-1])


def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
