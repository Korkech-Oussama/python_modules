#!/usr/bin/env python3
import sys


def arguments_handler():
    print("=== Command Quest ===")

    ac = len(sys.argv)
    path_parts = sys.argv[0].rpartition('/')
    program_name = path_parts[2] or sys.argv[0]
    if (ac == 1):
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {ac}")
    if ac > 1:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {ac - 1}")
        for i in range(1, ac):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {ac}")


if __name__ == "__main__":
    arguments_handler()
