"""Advent of Code 2023 day 2 solution."""
import numpy as np

colors = "red", "green", "blue"


def part1():
    """Returns answer to part 1 of the problem"""
    num_colors = np.array([12, 13, 14])
    counts = get_maxcounts("input1")

    ids = np.arange(1, len(counts) + 1)
    return np.sum(ids[np.all(counts <= num_colors, axis=1)])


def part2():
    """Returns answer to part 2 of the problem"""
    counts = get_maxcounts("input2")
    power = counts.prod(axis=1)
    return power.sum()


def get_maxcounts(datafile: str, part=1) -> np.ndarray:
    """
    Parses input data returning the maximum number of dice of each color seen in each game
    """
    with open(datafile, encoding="utf-8") as F:
        lines = F.readlines()

    counts = []
    for line in lines:
        for color in colors:
            if color in line:
                maxcount = max(int(l.split()[-1]) for l in line.split(color)[:-1])
                counts.append(maxcount)
            else:
                counts.append(0)

    counts = np.array(counts).reshape((len(counts) // 3, 3))
    return counts


def main():
    """Main function"""
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
