import logging
import os
from typing import List

logging.basicConfig(level=logging.DEBUG)


def read_input(input_filepath: str):
    input_file = open(input_filepath, "r")
    lines = input_file.readlines()

    result: List[str] = []
    for line in lines:
        result.append(line.strip())
    return result


def get_char_at_index(row: str, i: int):
    fixed_row = row
    while len(fixed_row) - 1 <= i:
        fixed_row += row
    return fixed_row[i]


def solve_1(rows: List[str]) -> int:
    current_index = 0
    tree_count = 0
    for row in rows:
        if current_index == 0:
            current_index += 3
            continue
        if get_char_at_index(row=row, i=current_index) == "#":
            tree_count += 1
        current_index += 3
    return tree_count


def solve_2(rows: List[str], right: int, down: int) -> int:
    char_index = right
    row_index = down
    tree_count = 0
    for ri in range(len(rows)):
        if ri != row_index:
            continue
        else:
            if get_char_at_index(row=rows[ri], i=char_index) == "#":
                tree_count += 1
            char_index += right
            row_index += down
    return tree_count


def run_1():
    input_filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    rows = read_input(input_filepath=input_filepath)
    result = solve_1(rows=rows)
    logging.debug(f"Found {result} trees.")


def run_2():
    input_filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    rows = read_input(input_filepath=input_filepath)
    res1 = solve_2(rows=rows, right=1, down=1)
    res2 = solve_2(rows=rows, right=3, down=1)
    res3 = solve_2(rows=rows, right=5, down=1)
    res4 = solve_2(rows=rows, right=7, down=1)
    res5 = solve_2(rows=rows, right=1, down=2)

    result = res1 * res2 * res3 * res4 * res5
    logging.debug(f"Product is {result}.")


if __name__ == "__main__":
    run_2()
