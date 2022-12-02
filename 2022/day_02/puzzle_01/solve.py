#!/usr/bin/env python3

from enum import Enum


class OpposedHand(Enum):
    Rock = "A"
    Paper = "B"
    Scissors = "C"


class OwnHand(Enum):
    Rock = "X"
    Paper = "Y"
    Scissors = "Z"


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
                opposed_hand, own_hand = line.split(" ")
                opposed_hand_name = OpposedHand(opposed_hand).name
                own_hand_name = OwnHand(own_hand).name
                if opposed_hand_name == own_hand_name:
                    total_score += ResultScore.Draw.value
                    if own_hand_name == "Rock":
                        total_score += ShapeScore.Rock.value
                    elif own_hand_name == "Paper":
                        total_score += ShapeScore.Paper.value
                    else:
                        total_score += ShapeScore.Scissors.value
                elif own_hand_name == "Rock":
                    total_score += ShapeScore.Rock.value
                    if opposed_hand_name == "Paper":
                        total_score += ResultScore.Loss.value
                    else:
                        total_score += ResultScore.Win.value
                elif own_hand_name == "Paper":
                    total_score += ShapeScore.Paper.value
                    if opposed_hand_name == "Rock":
                        total_score += ResultScore.Win.value
                    else:
                        total_score += ResultScore.Loss.value
                elif own_hand_name == "Scissors":
                    total_score += ShapeScore.Scissors.value
                    if opposed_hand_name == "Rock":
                        total_score += ResultScore.Loss.value
                    else:
                        total_score += ResultScore.Win.value
        print(total_score)


if __name__ == "__main__":
    main()
