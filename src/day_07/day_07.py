"""
Day 7: The Treachery of Whales
Goal: Compute the optimal horizontal position for crab submarines to align.
"""
import copy

INPUT_FILE = "../../data/day_07.txt"

if __name__ == "__main__":

    input_list = [int(element) for element in open(INPUT_FILE).readlines()[0].split(",")]

    print("#======= Part 1 =======#")

    best_position = min(input_list)
    score_best = max(input_list) * len(input_list)
    for position in range(min(input_list), max(input_list) + 1):
        score = sum([abs(element - position) for element in input_list])
        if score < score_best:
            score_best = score
            best_position = position

    print(f"Least consuming amount of fuel: {score_best} (for position {position})")

    print("#======= Part 2 =======#")

    best_position = min(input_list)
    score_best = max(input_list) * len(input_list) ** 2
    for position in range(min(input_list), max(input_list) + 1):
        score = sum(
            [abs(element - position) * (abs(element - position) + 1) / 2 for element in input_list]
        )
        if score < score_best:
            score_best = score
            best_position = position

    print(f"Least consuming amount of fuel: {score_best} (for position {position})")
