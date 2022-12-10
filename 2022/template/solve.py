#!/usr/bin/env python3


def puzzle01(path):
    """
    >>> puzzle01("./test_input_puzzle_01.txt")
    XXX
    """
    with open(path, encoding="utf-8") as file:
        #lines = file.read().split("\n\n")
        #lines = file.read().splitlines()
        #lines = list(filter(None, file.read().splitlines())) 
        result = 0
        for line in lines:

        return result


#def puzzle02(path):
#    """
#    >>> puzzle02("./test_input_puzzle_02.txt")
#    XXX
#    """
#    with open(path, encoding="utf-8") as file:
#        #lines = file.read().split("\n\n")
#        #lines = file.read().splitlines()
#        #lines = list(filter(None, file.read().splitlines())) 
#        result = 0
#        for line in lines:
#            pass
#
#        return result


def main():
    print(puzzle01("./input.txt"))
#    print(puzzle02("./input.txt"))


if __name__ == "__main__":
    main()
