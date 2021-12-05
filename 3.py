import requests as r
import pandas as pd


def load_data_from_url(url, user_session):
    raw_data = r.get(url, cookies={"session": user_session}).text
    return [x for x in raw_data.split("\n") if x]


# run_mode = ["less", "more"]
def extract_bit_values(parsed_input, run_mode: str = "less"):
    bit_values = []
    # Faster to take the sum of each bit column and if > 1/2 its more common,
    # but thats hard to read.
    for bit_idx, _ in enumerate(parsed_input[0]):
        n_zeros = len([i[bit_idx] for i in parsed_input if int(i[bit_idx]) == 0])
        n_ones = len([i[bit_idx] for i in parsed_input if int(i[bit_idx]) == 1])
        print({"n_zeros": n_zeros, "n_ones": n_ones})
        if run_mode == "less":
            if n_zeros > n_ones:
                bit_values.append(1)
            else:
                bit_values.append(0)
        if run_mode == "more":
            if n_zeros < n_ones:
                bit_values.append(1)
            else:
                bit_values.append(0)

    return bit_values


def binary_number_to_int(binary_number):
    return int(binary_number, 2)


data = load_data_from_url(
    url="https://adventofcode.com/2021/day/3/input",
    user_session="53616c7465645f5fe16aec55eeb76a9e3c0c14b618922a108ad609678c664b0e06cde4ca3558afd32a620072a42b8438",
)

# Part 1
gamma_bit_values = extract_bit_values(data, run_mode="more")
gamma_integer = binary_number_to_int("".join(str(x) for x in gamma_bit_values))

epsilon_bit_values = extract_bit_values(data, run_mode="less")
epsion_integer = binary_number_to_int("".join(str(x) for x in epsilon_bit_values))

print(
    {
        "gamma_integer": gamma_integer,
        "epsion_integer": epsion_integer,
        "power_consumption": gamma_integer * epsion_integer,
    }
)

# Part 2

life_support_rating = []
oxygen_generator_rating = []


def extract_complicated_bit_values(parsed_input, run_mode: str = "less"):
    # we will delete values from this as they become invalid
    valid_bit_indicies = [idx for idx in range(len(parsed_input))]
    for bit_idx, _ in enumerate(parsed_input[0]):
        column_values = [i[bit_idx] for i in parsed_input]
        n_zeros = len([i for i in column_values if int(i) == 0])
        n_ones = len([i for i in column_values if int(i) == 1])
        if run_mode == "less":
            
            
        if run_mode == "more":


        
