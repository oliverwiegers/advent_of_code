#!/usr/bin/env python3


def find_index(transmission, marker_size):
    marker = []
    for i,char in enumerate([*transmission], 1):
        if char not in marker:
            marker.append(char)
        else:
            marker = marker[marker.index(char)+1:]
            marker.append(char)
        if len(marker) == marker_size:
            return i


def puzzle01(path):
    """
    >>> puzzle01("./test_input_puzzle_01.txt")
    5
    >>> puzzle01("./input.txt")
    1566
    """
    with open(path, encoding="utf-8") as file:
        line = "".join(list(filter(None, file.read().splitlines())))
        return find_index(line, 4)


def puzzle02(path):
    """
    >>> puzzle02("./test_input_puzzle_02.txt")
    23
    >>> puzzle02("./input.txt")
    2265
    """
    with open(path, encoding="utf-8") as file:
        line = "".join(list(filter(None, file.read().splitlines())))
        start_index = find_index(line, 4)
        line = line[start_index:]
        return find_index(line, 14) + start_index


def main():
    print(puzzle01("./input.txt"))
    print(puzzle02("./input.txt"))


if __name__ == "__main__":
    main()
