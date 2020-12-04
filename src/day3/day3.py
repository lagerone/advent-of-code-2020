from typing import List


def read_input():
    input_file = open("inputs/input-day-3.txt", "r")
    lines = input_file.readlines()

    result: List[str] = []
    for line in lines:
        result.append(line.strip())
    return result


def run_1():
    entries = read_input()
    valid_pws: List[str] = []
    for row in entries:
        range, char_raw, password = row.split(" ")
        char = char_raw.replace(":", "")
        range_start, range_end = range.split("-")
        char_count = len(password) - len(password.replace(char, ""))
        if char_count >= int(range_start) and char_count <= int(range_end):
            valid_pws.append(password)

    print(f"Number of valid passwords: {len(valid_pws)}")


def run_2():
    entries = read_input()
    valid_pws: List[str] = []
    for row in entries:
        positions, char_raw, password = row.split(" ")
        char = char_raw.replace(":", "")
        first_position, second_position = positions.split("-")
        first_index = int(first_position) - 1
        second_index = int(second_position) - 1
        if password[first_index] == char and password[second_index] == char:
            continue
        if char in [password[first_index], password[second_index]]:
            valid_pws.append(password)
    print(f"Number of valid passwords: {len(valid_pws)}")


if __name__ == "__main__":
    run_2()