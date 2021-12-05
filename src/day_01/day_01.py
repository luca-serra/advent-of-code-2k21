"""
Day 1: Sonar Sweep
Goal: Find the number of increasing values.
"""

INPUT_FILE = "../../data/day_01.txt"

if __name__ == "__main__":

    input_list = [int(integer) for integer in open(INPUT_FILE).readlines()]

    # Part 1

    print("#======= Part 1 =======#")

    counter = 0
    previous_element = input_list[0]
    for element in input_list[1:]:
        if element > previous_element:
            counter += 1
        previous_element = element

    print(f"{counter} measurements are larger than the previous one.")

    print("#======= Part 2 =======#")

    counter = 0
    previous_element = sum(input_list[:3])
    for i in range(1, len(input_list) - 2):
        element = sum(input_list[i : i + 3])
        if element > previous_element:
            counter += 1
        previous_element = element

    print(f"{counter} measurements are larger than the previous one.")
