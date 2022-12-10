#!/usr/bin/env python3


def calc_signal_strength(result, register, cycles, count=1):
    for _ in range(count):
        cycles += 1
        if cycles == 20 or (cycles - 20) % 40 == 0:
            result += cycles * register
    return result, cycles


def puzzle01(path):
    """
    >>> puzzle01("./test_input_puzzle_01.txt")
    13140
    >>> puzzle01("./input.txt")
    14560
    """
    with open(path, encoding="utf-8") as file:
        lines = list(filter(None, file.read().splitlines()))
        result = 0
        cycles = 0
        register = 1
        for line in lines:
            try:
                _, value = line.split(" ")
                result, cycles = calc_signal_strength(result, register, cycles, 2)
                register += int(value)
            except:
                result, cycles = calc_signal_strength(result, register, cycles)

        return result


def puzzle02(path):
    """
    >>> puzzle02("./test_input_puzzle_02.txt")
    ##..##..##..##..##..##..##..##..##..##..
    ###...###...###...###...###...###...###.
    ####....####....####....####....####....
    #####.....#####.....#####.....#####.....
    ######......######......######......####
    #######.......#######.......#######.....
    >>> puzzle02("./input.txt")
    ####.#..#.###..#..#.####.###..#..#.####.
    #....#.#..#..#.#..#.#....#..#.#..#....#.
    ###..##...#..#.####.###..#..#.#..#...#..
    #....#.#..###..#..#.#....###..#..#..#...
    #....#.#..#.#..#..#.#....#....#..#.#....
    ####.#..#.#..#.#..#.####.#.....##..####.
    """
    with open(path, encoding="utf-8") as file:
        lines = list(filter(None, file.read().splitlines()))
        register = 1
        crt = []

        for line in lines:
            try:
                value = int(line.split(" ")[1])
                crt.append(register)
                crt.append(register)
                register += value
            except:
                crt.append(register)

        for section in range(0, len(crt), 40):
            row = ""
            for column in range(40):
                if abs(crt[section + column] - column) <= 1:
                    row += "#"
                else:
                    row += "."
            print(row)


def main():
    print(puzzle01("./input.txt"))
    puzzle02("./input.txt")


if __name__ == "__main__":
    main()
