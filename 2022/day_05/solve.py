#!/usr/bin/env python3


def puzzle01(path):
    """
    >>> puzzle01("./test_input_puzzle_01.txt")
    'CMZ'
    """
    with open(path, encoding="utf-8") as file:
        result = ""
        cargo_plan = file.read().split("\n\n")
        cargo = []

        [cargo.append(a) for a in cargo_plan[0].split("\n")]
        rotated = [list(a) for a in list(zip(*cargo[::-1]))]
        cleaned = [item for item in rotated if item[0].isnumeric()]

        stacks = {}
        for stack in cleaned:
            stack = list(filter(None, [r.strip(" ") for r in stack]))
            stack.reverse()
            stacks[int(stack.pop(len(stack) - 1))] = stack

        for line in cargo_plan[1].split("\n"):
            count, source, target = [int(s) for s in line.split() if s.isnumeric()]
            for _ in range(count):
                stacks[target].insert(0, stacks[source].pop(0))

        for _, stack in stacks.items():
            result += stack.pop(0)

        return result


def puzzle02(path):
    """
    >>> puzzle02("./test_input_puzzle_02.txt")
    'MCD'
    """
    with open(path, encoding="utf-8") as file:
        result = ""
        cargo_plan = file.read().split("\n\n")
        cargo = []

        [cargo.append(a) for a in cargo_plan[0].split("\n")]
        rotated = [list(a) for a in list(zip(*cargo[::-1]))]
        cleaned = [item for item in rotated if item[0].isnumeric()]

        stacks = {}
        for stack in cleaned:
            stack = list(filter(None, [r.strip(" ") for r in stack]))
            stack.reverse()
            stacks[int(stack.pop(len(stack) - 1))] = stack

        for line in cargo_plan[1].split("\n"):
            count, source, target = [int(s) for s in line.split() if s.isnumeric()]
            if count == 1:
                stacks[target].insert(0, stacks[source].pop(0))
            else:
                temp = []
                for _ in range(count):
                    temp.append(stacks[source].pop(0))

                stacks[target] = temp + stacks[target]

        for _, stack in stacks.items():
            result += stack.pop(0)

        return result


def main():
    print(puzzle01("./input.txt"))
    print(puzzle02("./input.txt"))


if __name__ == "__main__":
    main()
