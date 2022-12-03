#!/usr/bin/env python3

import string


def divide_groups(listing, length):
    for i in range(0, len(listing), length):
        yield listing[i : i + length]


def main():
    priorities = {}
    for index, letter in enumerate(string.ascii_letters, 1):
        priorities[letter] = index

    with open("./input.txt", encoding="utf-8") as file:
        priorities_summed = 0
        elves = file.read().splitlines()
        groups = divide_groups(elves, 3)

        for group in groups:
            badge = set(group[0]) & set(group[1]) & set(group[2])
            # There is only one item so we don't need to iterate over the set.
            priorities_summed += priorities.get(badge.pop())

        print(priorities_summed)


if __name__ == "__main__":
    main()
