"""
Day 4: Giant Squid
Goal: Find the winning board of Bingo.
"""
import numpy as np
import copy

INPUT_FILE = "../../data/day_04.txt"

if __name__ == "__main__":

    input_list = [str(element) for element in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"

    print("#======= Part 1 =======#")

    numbers = [int(number) for number in input_list[0].split(",")]
    grids = []
    grid = []
    stop = False
    for element in input_list[2:]:
        if element == "\n":
            stop = True
            grid = np.array(grid)
            grids.append(grid)
            grid = []
        else:
            grid.append([int(number) for number in element[:-1].split()])
        stop = False

    side = grids[0].shape[0]
    winning_number = None
    winning_grid = None
    winning_index = None

    for idx in range(len(numbers)):
        if winning_number:
            winning_index = idx - 1
            break
        used_numbers = numbers[: idx + 1]
        for grid in grids:
            if winning_number:
                break
            for i in range(side):
                if len(set(used_numbers).intersection(set(grid[i, :]))) == side:
                    winning_number = numbers[idx]
                    winning_grid = grid
                    break
            for j in range(side):
                if len(set(used_numbers).intersection(set(grid[:, j]))) == side:
                    winning_number = numbers[idx]
                    winning_grid = grid
                    break

    result = sum(
        [
            winning_grid[i, j]
            for i in range(side)
            for j in range(side)
            if winning_grid[i, j] not in numbers[: winning_index + 1]
        ]
    )

    print(f"Product of winning board elements and last number: {result * winning_number}")

    print("#======= Part 2 =======#")

    winning_number = None
    winning_grid = None
    winning_index = None
    remaining_grids = copy.deepcopy(grids)

    for idx in range(len(numbers)):
        if winning_number and len(remaining_grids) == 1:
            winning_index = idx - 1
            break
        used_numbers = numbers[: idx + 1]
        grid_idx = 0
        while grid_idx < len(remaining_grids) - 1:
            grid = remaining_grids[grid_idx]
            if winning_number and len(remaining_grids) == 1:
                break
            for i in range(side):
                if len(set(used_numbers).intersection(set(grid[i, :]))) == side:
                    winning_number = numbers[idx]
                    winning_grid = grid
                    remaining_grids.pop(grid_idx)
                    break
            for j in range(side):
                if len(set(used_numbers).intersection(set(grid[:, j]))) == side:
                    winning_number = numbers[idx]
                    winning_grid = grid
                    remaining_grids.pop(grid_idx)
                    break
            grid_idx += 1

    result = sum(
        [
            winning_grid[i, j]
            for i in range(side)
            for j in range(side)
            if winning_grid[i, j] not in numbers[: winning_index + 1]
        ]
    )

    print(f"Product of winning board elements and last number: {result * winning_number}")
