#!/usr/bin/env python3

from collections import deque
from math import inf


# Actual logic for puzzle01
def check_neighbors(grid, row, column):
    elevation = grid[row][column] + 1
    height = len(grid)
    width = len(grid[0])

    for nrow, ncolumn in (
        (row + 1, column),
        (row - 1, column),
        (row, column + 1),
        (row, column - 1),
    ):
        if 0 <= nrow < height and 0 <= ncolumn < width:
            if grid[nrow][ncolumn] <= elevation:
                yield nrow, ncolumn


def bfs(grid, src, dest):
    queue = deque([(0, src)])
    visited = set()

    while queue:
        distance, row_column = queue.popleft()
        row, column = row_column

        if row_column == dest:
            return distance

        if row_column not in visited:
            visited.add(row_column)

            for neighbor in check_neighbors(grid, row, column):
                if neighbor in visited:
                    continue

                queue.append((distance + 1, neighbor))

    return inf


def puzzle01(path):
    """
    >>> puzzle01("./test_input_puzzle_01.txt")
    31
    >>> puzzle01("./input.txt")
    412
    """
    with open(path, "rb") as file:
        lines = list(filter(None, file.read().splitlines()))
    grid = list(map(list, lines))
    start, end, lowest, highest = b"SEaz"
    src = None
    dest = None

    for row, line in enumerate(grid):
        for column, cell in enumerate(line):
            if cell == start:
                src = row, column
                grid[row][column] = lowest
            elif cell == end:
                dest = row, column
                grid[row][column] = highest

        if src and dest:
            break

    return bfs(grid, src, dest)


def puzzle02(path):
    """
    >>> puzzle02("./test_input_puzzle_02.txt")
    29
    >>> puzzle02("./input.txt")
    402
    """
    with open(path, "rb") as file:
        lines = list(filter(None, file.read().splitlines()))

    grid = list(map(list, lines))
    start, end, lowest, highest = b"SEaz"
    sources = set()
    dest = None

    for row, line in enumerate(grid):
        for column, cell in enumerate(line):
            if cell == start:
                grid[row][column] = lowest
                sources.add((row, column))
            elif cell == lowest:
                sources.add((row, column))
            elif cell == end:
                dest = row, column
                grid[row][column] = highest

    return min([bfs(grid, x, dest) for x in sources])


def main():
    print(puzzle01("./input.txt"))
    print(puzzle02("./input.txt"))


if __name__ == "__main__":
    main()
