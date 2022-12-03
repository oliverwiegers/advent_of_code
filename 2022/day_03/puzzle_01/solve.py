#!/usr/bin/env python3

import string


def main():
    priorities = {}
    for index, letter in enumerate(string.ascii_lowercase, 1):
        priorities[letter] = index

    for index, letter in enumerate(string.ascii_uppercase, 27):
        priorities[letter] = index

    with open("./input.txt") as file:
        priorities_summed = 0
        lines = file.readlines()
        for line in lines:
            if line:
                line = line.strip()
                n = len(line)
                s1 = slice(0, n // 2)
                s2 = slice(n // 2, n)
                first = line[s1]
                second = line[s2]
                allready_checked = []

                for letter in first:
                    if letter not in allready_checked:
                        if letter in second:
                            allready_checked.append(letter)
                            priorities_summed += priorities.get(letter)

        print(priorities_summed)


if __name__ == "__main__":
    main()
