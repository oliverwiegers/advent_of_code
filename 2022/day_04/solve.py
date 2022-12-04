#!/usr/bin/env python3


def puzzle01(path):
    """
    >>> puzzle01("./test_input_puzzle_01.txt")
    2
    >>> puzzle01("./input.txt")
    448
    """
    with open(path, encoding="utf-8") as file:
        result = 0
        lines = file.read().splitlines()
        for line in lines:
            if line:
                a1, a2, b1, b2 = map(int, line.replace("-", ",").split(","))

                if set(range(a1, a2 + 1)) <= set(range(b1, b2 + 1)):
                    result += 1
                elif set(range(b1, b2 + 1)) <= set(range(a1, a2 + 1)):
                    result += 1

        return result


def puzzle02(path):
    """
    >>> puzzle02("./test_input_puzzle_02.txt")
    4
    >>> puzzle02("./input.txt")
    794
    """
    with open(path, encoding="utf-8") as file:
        result = 0
        lines = file.read().splitlines()
        for line in lines:
            if line:
                a1, a2, b1, b2 = map(int, line.replace("-", ",").split(","))

                if set(range(a1, a2 + 1)) & set(range(b1, b2 + 1)):
                    result += 1

        return result


def main():
    print(puzzle01("./input.txt"))
    print(puzzle02("./input.txt"))


if __name__ == "__main__":
    main()
