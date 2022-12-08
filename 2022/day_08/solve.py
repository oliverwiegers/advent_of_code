#!/usr/bin/env python3


def puzzle01(path):
    """
    >>> puzzle01("./test_input_puzzle_01.txt")
    21
    >>> puzzle01("./input.txt")
    1845
    """
    with open(path, encoding="utf-8") as file:
        lines = list(filter(None, file.read().splitlines()))
        grid = []
        for line in lines:
            grid.append(list(line))

        result = len(grid) * 2 + len(lines) * 2 - 4
        for index, line in enumerate(grid):
            if index == 0:
                continue
            if index == len(grid) - 1:
                continue

            for i, tree in enumerate(line):
                if i == 0:
                    continue
                if i == len(line) - 1:
                    continue

                # Check left
                if max(set(line[:i])) < tree:
                    result += 1
                    continue
                # Check right
                if max(set(line[i+1:])) < tree:
                    result += 1
                    continue

                column = []
                for column_line in grid:
                    column.append(column_line[i])
                if max(set(column[:index])) < tree:
                    result += 1
                    continue
                if max(set(column[index+1:])) < tree:
                    result += 1
                    continue

        return result


def puzzle02(path):
    """
    >>> puzzle02("./test_input_puzzle_02.txt")
    8
    >>> puzzle02("./input.txt")
    230112
    """
    with open(path, encoding="utf-8") as file:
        result = 0
        lines = list(filter(None, file.read().splitlines()))
        grid = []

        for line in lines:
            grid.append(list(line))

        for index, line in enumerate(grid):
            for i, tree in enumerate(line):
                column = []
                for row in grid:
                    column.append(row[i])

                top = 0
                left = 0
                right = 0
                bottom = 0

                # Check left
                if i == 0:
                    left = 0
                else:
                    if max(set(line[:i])) < tree:
                        left = i
                    else:
                        for count in line[:i][::-1]:
                            left += 1
                            if count >= tree:
                                break

                # Check right
                if i == len(line) - 1:
                    right = 0
                else:
                    if max(set(line[i+1:])) < tree:
                        right = len(line) - i - 1
                    else:
                        for count in line[i+1:]:
                            right += 1
                            if count >= tree:
                                break

                # Check up
                if index == 0:
                    top = 0
                else:
                    if max(set(column[:index])) < tree:
                        top = index
                    else:
                        for count in column[:index][::-1]:
                            top += 1
                            if count >= tree:
                                break

                # Check down
                if index == len(grid) - 1:
                    bottom = 0
                else:
                    if max(set(column[index+1:])) < tree:
                        bottom = len(grid) - index - 1
                    else:
                        for count in column[index+1:]:
                            bottom += 1
                            if count >= tree:
                                break

                score = top * left * right * bottom
                if score > result:
                    result = score

        return result


def main():
    print(puzzle01("./input.txt"))
    print(puzzle02("./input.txt"))


if __name__ == "__main__":
    main()
