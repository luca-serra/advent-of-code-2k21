"""
Day 5: Hydrothermal Venture
Goal: Find overlapping lines.
"""

from src.day_05.utils import get_coordinates_between

INPUT_FILE = "../../data/day_05.txt"

if __name__ == "__main__":

    input_list = [str(element) for element in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = input_list = [string[:-1] for string in input_list]

    elements = []

    for element in input_list:
        start, end = element.split(" -> ")
        elements.append(
            (
                (int(start.split(",")[0]), int(start.split(",")[-1])),
                (int(end.split(",")[0]), int(end.split(",")[-1])),
            )
        )

    print("#======= Part 1 & 2 =======#")

    line_counts = {}
    line_counts_2 = {}

    for line in elements:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            points = get_coordinates_between(*line[0], *line[1])
            for point in points:
                if str(point) in line_counts:
                    line_counts[str(point)] += 1
                else:
                    line_counts[str(point)] = 1

                if str(point) in line_counts_2:
                    line_counts_2[str(point)] += 1
                else:
                    line_counts_2[str(point)] = 1
        else:
            points = get_coordinates_between(*line[0], *line[1], simplified=False)
            for point in points:
                if str(point) in line_counts_2:
                    line_counts_2[str(point)] += 1
                else:
                    line_counts_2[str(point)] = 1

    n_dangerous = 0
    n_dangerous_2 = 0

    for point, count in line_counts.items():
        if count >= 2:
            n_dangerous += 1
    for point, count in line_counts_2.items():
        if count >= 2:
            n_dangerous_2 += 1

    print(get_coordinates_between(9, 7, 7, 9, simplified=False))

    print(f"(Part 1) Number of dangerous points: {n_dangerous}")
    print(f"(Part 2) Number of dangerous points: {n_dangerous_2}")
