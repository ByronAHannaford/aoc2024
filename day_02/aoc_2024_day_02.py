# Advent of Code 2024
# Day 02
# Byron

import argparse
import logging
import sys

from pathlib import Path

PARENT_FOLDER = Path(__file__).parent
BASE_FILE_NAME = Path(__file__).stem
INPUT_FILE_NAME = f"{BASE_FILE_NAME}_input.txt"
SAMPLE_FILE_NAME = f"{BASE_FILE_NAME}_sample.txt"

INPUT_PATH = PARENT_FOLDER / INPUT_FILE_NAME
SAMPLE_PATH = PARENT_FOLDER / SAMPLE_FILE_NAME


logger = logging.getLogger("aoc_logger")
log_handler = logging.StreamHandler()
log_handler.setLevel("DEBUG")
logger.addHandler(log_handler)


# ---=== PROBLEM CODE BELOW ===---


def parse_input(data_path: Path) -> list:
    """
    Reads and formats input.
    Should return the input data in a format where it is ready to be worked on.
    """
    with open(data_path, "r") as raw_input:
        return [l.strip() for l in raw_input.readlines()]

def isLineSafe(numbers: list[int], problemDampener = False, problemDampenerUsed = False) -> bool:
    print(numbers)
    if len(numbers) < 2:
        return False  # Not enough numbers to compare

    increasing = numbers[0] < numbers[1]

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if increasing:
            if diff <= 0 or diff > 3:
                if(problemDampener and not problemDampenerUsed):               
                    return removeOneNumber(numbers)
                else:
                    return False
        else:
            if diff >= 0 or diff < -3:
                if(problemDampener and not problemDampenerUsed):
                    return removeOneNumber(numbers)
                else:
                    return False

    return True

def removeOneNumber(numbers: list[int]):
    for i in range(len(numbers)):
        # Create a new list with the i-th number removed
        new_numbers = numbers[:i] + numbers[i+1:]
        # Check if the new list is safe
        if isLineSafe(new_numbers, True, True):
            return True
    return False

def part_1(input_data: list):
            
    """Solution code for Part 1. Should return the solution."""
    return sum(1 for line in input_data if isLineSafe(list(map(int, line.split()))))


def part_2(input_data: list):
    """Solution code for Part 2. Should return the solution."""
    return sum(1 for line in input_data if isLineSafe(list(map(int,line.split())), True))


def run_direct():
    """
    This function runs if this file is executed directly, rather than using the
    justfile interface. Useful for quick debugging and checking your work.
    """
    print(parse_input(SAMPLE_PATH))


# ---=== PROBLEM CODE ABOVE ===---


def problem_dispatch(mode: str, part: int, log_level: str = None):
    if log_level is not None:
        logger.setLevel(log_level.upper())
    parts = {1: part_1, 2: part_2}
    inputs = {"check": parse_input(SAMPLE_PATH), "solve": parse_input(INPUT_PATH)}
    return parts[part](inputs[mode])


def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=str, choices={"check", "solve"})
    parser.add_argument("part", type=int, choices={1, 2})
    parser.add_argument(
        "--log-level",
        type=str,
        required=False,
        choices={"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"},
    )
    args = parser.parse_args()
    print(problem_dispatch(args.mode, args.part, args.log_level))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise SystemExit(run_direct())
    else:
        raise SystemExit(run_cli())
