#!/usr/bin/env python3


def main():
    # 1. Open input file
    # 2. Split by empty line
    # 3. Remove empty items (last item), sum up inventory per elf, sort list,
    #    get three highest values, print the sum.
    with open("./input.txt") as file:
        lines = file.read()
        elves = lines.split("\n\n")
        # puzzle 01 was:
        # print(
        #    max(
        #        [
        #            sum([int(x) for x in elf.split("\n")])
        #            for elf in list(filter(None, elves))
        #        ]
        #    )
        # )
        print(
            sum(
                sorted(
                    [
                        sum([int(x) for x in elf.split("\n")])
                        for elf in list(filter(None, elves))
                    ],
                    reverse=True,
                )[:3]
            )
        )


if __name__ == "__main__":
    main()
