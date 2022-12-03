#!/usr/bin/env python3


def divide_groups(listing, length):
    """
    Helper function for puzzle 02 to split elves into groups.
    """
    for i in range(0, len(listing), length):
        yield listing[i : i + length]


def puzzle01(path):
    """
    >>> puzzle01("./test_input_puzzle_01.txt")
    157
    """
    priorities = {}
    for index, letter in enumerate(string.ascii_letters, 1):
        priorities[letter] = index

    with open(path, encoding="utf-8") as file:
        priorities_summed = 0
        backpacks = file.read().splitlines()
        for backpack in backpacks:
            divider = len(backpack) // 2
            duplicate_items = set(backpack[:divider]).intersection(
                set(backpack[divider:])
            )

            for item in duplicate_items:
                priorities_summed += priorities.get(item)

        return priorities_summed


def puzzle02(path):
    """
    >>> puzzle02("./test_input_puzzle_02.txt")
    70
    """
    priorities = {}
    for index, letter in enumerate(string.ascii_letters, 1):
        priorities[letter] = index

    with open(path, encoding="utf-8") as file:
        priorities_summed = 0
        elves = file.read().splitlines()
        groups = divide_groups(elves, 3)

        for group in groups:
            badge = set(group[0]) & set(group[1]) & set(group[2])
            # There is only one item so we don't need to iterate over the set.
            priorities_summed += priorities.get(badge.pop())

        return priorities_summed


def main():
    print(puzzle01("./input.txt"))
    print(puzzle02("./input.txt"))


if __name__ == "__main__":
    main()
