#!/usr/bin/env python3


def puzzle01(path):
    """
    >>> puzzle01("./test_input_puzzle_01.txt")
    XXX
    """
    with open(path, encoding="utf-8") as file:
        result = 0
        lines = file.read().splitlines()
        for line in lines:

        return result


def puzzle02(path):
    """
    >>> puzzle02("./test_input_puzzle_02.txt")
    XXX
    """
    with open(path, encoding="utf-8") as file:
        result = 0
        lines = file.read().splitlines()
        for line in lines:

        return result


def main():
    print(puzzle01("./input.txt"))
    print(puzzle02("./input.txt"))


if __name__ == "__main__":
    main()
