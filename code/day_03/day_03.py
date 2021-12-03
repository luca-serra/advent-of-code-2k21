"""
Day 1: Binary Diagnostic
Goal: Find the most common bits and perform operations.
"""

import copy
from math import ceil, floor

INPUT_FILE = "../../data/day_03.txt"

if __name__ == "__main__":

    input_list = [str(element) for element in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = input_list = [string[:-1] for string in input_list]

    size = len(input_list)
    n_bits = len(input_list[0])

    print("#======= Part 1 =======#")

    gamma = 0
    epsilon = 0

    for i in range(n_bits):
        gamma += (sum([int(binary[i]) for binary in input_list]) > size / 2) * 2 ** (
            n_bits - (i + 1)
        )
        epsilon += (sum([int(binary[i]) for binary in input_list]) < size / 2) * 2 ** (
            n_bits - (i + 1)
        )

    print(f"Product of gamma and epsilon rates: {gamma * epsilon}")

    print("#======= Part 2 =======#")

    oxygen_rating = ""
    co2_rating = ""

    # For oxygen

    n_remaining = size
    list_remaining = copy.deepcopy(input_list)
    bit_to_consider = 0

    while n_remaining > 1:
        most_common = 1 * (
            sum([int(element[bit_to_consider]) for element in list_remaining])
            >= ceil(n_remaining / 2)
        )
        most_common = str(most_common)
        list_remaining = [
            element for element in list_remaining if element[bit_to_consider] == most_common
        ]
        n_remaining = len(list_remaining)
        bit_to_consider += 1

    oxygen_rating = list_remaining[0]

    # For C02

    n_remaining = size
    list_remaining = copy.deepcopy(input_list)
    bit_to_consider = 0

    while n_remaining > 1:
        least_common = 1 * (
            sum([int(element[bit_to_consider]) for element in list_remaining]) < n_remaining / 2
        )

        least_common = str(least_common)
        list_remaining = [
            element for element in list_remaining if element[bit_to_consider] == least_common
        ]
        n_remaining = len(list_remaining)
        bit_to_consider += 1

    co2_rating = list_remaining[0]

    oxygen_decimal_rating = 0
    co2_decimal_rating = 0

    for i in range(n_bits):
        oxygen_decimal_rating += int(oxygen_rating[i]) * 2 ** (n_bits - (i + 1))
        co2_decimal_rating += int(co2_rating[i]) * 2 ** (n_bits - (i + 1))

    print(oxygen_decimal_rating, co2_decimal_rating, co2_decimal_rating * oxygen_decimal_rating)
