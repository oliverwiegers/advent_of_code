#!/usr/bin/env python3

from enum import Enum


class OpposedHand(Enum):
    Rock = "A"
    Paper = "B"
    Scissors = "C"


class Outcome(Enum):
    Loss = "X"
    Draw = "Y"
    Win = "Z"


class ShapeScore(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class ResultScore(Enum):
    Loss = 0
    Draw = 3
    Win = 6


def main():
    with open("./input.txt") as file:
        lines = file.read()
        total_score = 0
        for line in lines.split("\n"):
            if line:
                opposed_hand, outcome = line.split(" ")
                opposed_hand_name = OpposedHand(opposed_hand).name
                outcome_name = Outcome(outcome).name
                if outcome_name == "Draw":
                    total_score += ResultScore.Draw.value
                    if opposed_hand_name == "Rock":
                        total_score += ShapeScore.Rock.value
                    elif opposed_hand_name == "Paper":
                        total_score += ShapeScore.Paper.value
                    else:
                        total_score += ShapeScore.Scissors.value
                elif outcome_name == "Loss":
                    total_score += ResultScore.Loss.value
                    if opposed_hand_name == "Rock":
                        total_score += ShapeScore.Scissors.value
                    elif opposed_hand_name == "Paper":
                        total_score += ShapeScore.Rock.value
                    else:
                        total_score += ShapeScore.Paper.value
                else:
                    total_score += ResultScore.Win.value
                    if opposed_hand_name == "Rock":
                        total_score += ShapeScore.Paper.value
                    elif opposed_hand_name == "Paper":
                        total_score += ShapeScore.Scissors.value
                    else:
                        total_score += ShapeScore.Rock.value

        print(total_score)


if __name__ == "__main__":
    main()
