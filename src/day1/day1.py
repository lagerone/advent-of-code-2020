import os
from typing import List


def read_input():
    input_filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    input_file = open(input_filepath, "r")
    lines = input_file.readlines()

    result: List[str] = []
    for line in lines:
        result.append(line.strip())
    return result


def run_1():
    entries = read_input()

    success = False
    for i in range(len(entries)):
        first_number = int(entries[i])
        for ii in range(len(entries)):
            if i == ii:
                continue
            second_number = int(entries[ii])
            if first_number + second_number == 2020:
                success = True
                print(f"{first_number} + {second_number} = 2020")
                print(
                    f"{first_number} * {second_number} = {first_number * second_number}"
                )
                break
        if success:
            break


def run_2():
    entries = read_input()

    success = False
    for i in range(len(entries)):
        first_number = int(entries[i])
        for ii in range(len(entries)):
            if i == ii:
                continue
            second_number = int(entries[ii])
            for iii in range(len(entries)):
                if iii in [i, ii]:
                    continue
                third_number = int(entries[iii])
                if first_number + second_number + third_number == 2020:
                    success = True
                    print(f"{first_number} + {second_number} + {third_number} = 2020")
                    print(
                        f"{first_number} * {second_number} * {third_number} = {first_number * second_number * third_number}"
                    )
                    break
            if success:
                break
        if success:
            break


if __name__ == "__main__":
    run_2()