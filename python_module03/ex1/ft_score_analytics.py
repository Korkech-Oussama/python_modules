#!/usr/bin/env python3
import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")

    ac = len(sys.argv)
    score_sum = 0
    if ac == 1:
        print("No scores provided. Usage: python3" +
              "ft_score_analytics.py <score1> <score2> ...")
    elif ac > 1:
        score_list: list[int] = []
        try:
            for i in range(1, ac):
                score_list.append(int(sys.argv[i]))
                score_sum += int(sys.argv[i])
        except ValueError:
            print(f"oops, I typed ’{sys.argv[i]}’")
        else:
            print(f"Scores processed: {score_list}")
            print(f"Total players: {ac - 1}")
            print(f"Total score: {score_sum}")
            print(f"Average score: {score_sum / (ac - 1)}")
            print(f"High score: {max(score_list)}")
            print(f"Low score: {min(score_list)}")
            print(f"Score range: {max(score_list) - min(score_list)}")


if __name__ == "__main__":
    score_analytics()
