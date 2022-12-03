#!/usr/bin/env python3

import string


def divide_groups(listing, length):
    for i in range(0, len(listing), length):
        yield listing[i : i + length]


def main():
    priorities = {}
    for index, letter in enumerate(string.ascii_lowercase, 1):
        priorities[letter] = index

    for index, letter in enumerate(string.ascii_uppercase, 27):
        priorities[letter] = index

    with open("./input.txt") as file:
        priorities_summed = 0
        lines = file.readlines()

        group_size = 3
        groups = divide_groups(lines, group_size)

        for group in groups:
            allready_checked = []
            group = [member.strip() for member in group]
            first, second, third = group

            for item in first:
                if item not in allready_checked:
                    allready_checked.append(item)
                    if item in second:
                        if item in third:
                            priorities_summed += priorities.get(item)

        print(priorities_summed)


if __name__ == "__main__":
    main()
