#!/usr/bin/env python3

import string


def main():
    priorities = {}
    for index, letter in enumerate(string.ascii_letters, 1):
        priorities[letter] = index

    with open("./input.txt", encoding="utf-8") as file:
        priorities_summed = 0
        backpacks = file.read().splitlines()
        for backpack in backpacks:
            divider = len(backpack) // 2
            duplicate_items = set(backpack[:divider]).intersection(
                set(backpack[divider:])
            )

            for item in duplicate_items:
                priorities_summed += priorities.get(item)

        print(priorities_summed)


if __name__ == "__main__":
    main()
