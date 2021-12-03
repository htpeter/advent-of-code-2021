import requests as r
import pandas as pd


def load_data_from_url(url, user_session):
    raw_data = r.get(url, cookies={"session": user_session}).text
    return [x for x in raw_data.split("\n") if x]


def adjust_position_part_1(instruction_set: list, position: list):
    for inst in instruction_set:
        i = inst.split(" ")
        direction, value = i[0], i[-1]
        if direction == "forward":
            position[0] += int(value)
        if direction == "up":
            position[1] += int(value)
        if direction == "down":
            position[1] -= int(value)
    return position


def adjust_position_part_2(instruction_set: list, position: list):
    """
    position[0] = horizontal position,
    position[1] = vertical position,
    position[2] = aiming direction
    """
    for inst in instruction_set:
        i = inst.split(" ")
        direction, value = i[0], i[-1]
        if direction == "forward":
            position[0] += int(value)
            position[1] += int(value) * position[2]
        if direction == "up":
            position[2] -= int(value)
        if direction == "down":
            position[2] += int(value)
    return position


puzzle_input_url = "https://adventofcode.com/2021/day/2/input"
my_user_session = "YOUR_SESSION_HERE"


# Part 1
starting_position = [0, 0]
part_1_data = load_data_from_url(puzzle_input_url, my_user_session)
final_position = adjust_position_part_1(part_1_data, starting_position)
print(f"Final position: {final_position}")
# had this inverted in Part 1 so I had to flip it
part_1_result = final_position[0] * -final_position[1]
print(f"Part 1 result: {part_1_result}")

# Part 2
starting_position = [0, 0, 0]
part_2_data = load_data_from_url(puzzle_input_url, my_user_session)
final_position = adjust_position_part_2(part_2_data, starting_position)
print(f"Final position: {final_position}")
part_2_result = final_position[0] * final_position[1]
print(f"Part 2 result: {part_2_result}")
