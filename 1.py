import requests as r
import pandas as pd


def load_data_from_url(url, user_session):
    raw_data = r.get(url, cookies={"session": user_session}).text
    return [int(x) for x in raw_data.split("\n") if x]


def rolling_window_increase_counter(depths: list, rolling_window_size: int):
    result = []
    depths = pd.DataFrame({"depth_reading": depths})
    depths["rolling_window"] = (
        depths["depth_reading"].rolling(rolling_window_size).sum()
    )
    depths["prior_window_value"] = depths["rolling_window"].shift(1)
    for idx, row in depths.iterrows():
        if idx + 1 < rolling_window_size:
            continue
        elif row["rolling_window"] > row["prior_window_value"]:
            result.append("increased")
        elif row["rolling_window"] < row["prior_window_value"]:
            result.append("decreased")
    return result


puzzle_input_url = "https://adventofcode.com/2021/day/1/input"
my_user_session = "YOUR_SESSION_HERE"

# Part 1 - # w/ my User Session's data 1477
part_1_puzzle_input = load_data_from_url(puzzle_input_url, my_user_session)
part_1_result = rolling_window_increase_counter(part_1_puzzle_input, 1)
print("part 1 answer")
print(len([i for i in part_1_result if i == "increased"]))

# Part 2 - # w/ my User Session's data 1523
part_2_data_url = "https://adventofcode.com/2021/day/1/input"
part_2_puzzle_input = load_data_from_url(puzzle_input_url, my_user_session)
part_2_result = rolling_window_increase_counter(part_2_puzzle_input, 3)
print("part 2 answer")
print(len([i for i in part_2_result if i == "increased"]))
