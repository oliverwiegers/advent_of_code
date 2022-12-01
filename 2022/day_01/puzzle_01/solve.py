#!/usr/bin/env python3


def main():
    # 1. Open input file
    # 2. Split by empty line
    # 3. Remove empty items (last item), sum up inventory per elf, print highest
    #    value
    with open("./input.txt") as file:
        lines = file.read()
        elves = lines.split("\n\n")
        print(
            max(
                [
                    sum([int(x) for x in elf.split("\n")])
                    for elf in list(filter(None, elves))
                ]
            )
        )


if __name__ == "__main__":
    main()
