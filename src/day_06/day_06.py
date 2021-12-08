"""
Day 6: Lanternfish
Goal: Count the number of lantern fishes.
"""
import copy

INPUT_FILE = "../../data/day_06.txt"

if __name__ == "__main__":

    input_list = [int(element) for element in open(INPUT_FILE).readlines()[0].split(",")]

    print("#======= Part 1 =======#")

    current_fishes = copy.deepcopy(input_list)
    new_fishes = []

    for day in range(1, 81):
        for i in range(len(current_fishes)):
            if current_fishes[i] == 0:
                new_fishes.append(8)
                current_fishes[i] = 6
            else:
                current_fishes[i] -= 1
        current_fishes += new_fishes
        new_fishes = []

    print(f"Number of fishes after 80 days: {len(current_fishes)}")

    def number_of_fishes(initial_number: int, days: int):
        if days <= initial_number:
            return [initial_number - days]
        else:
            if (initial_number - days) % 7

    # print(
    #     2 * len(number_of_fishes(3, 80))
    #     + len(number_of_fishes(4, 80))
    #     + len(number_of_fishes(1, 80))
    #     + len(number_of_fishes(2, 80))
    # )
    # def number_of_fishes(initial_number: int, days: int):

    print(number_of_fishes(3, 21))
