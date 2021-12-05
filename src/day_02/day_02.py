"""
Day 2: Dive!
Goal: Calculate the coordinates of a submarine.
"""

INPUT_FILE = "../../data/day_02.txt"

if __name__ == "__main__":

    input_list = [str(element) for element in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = input_list = [string[:-1] for string in input_list]

    print("#======= Part 1 =======#")

    horizon_depth = [0, 0]
    for instruction in input_list:
        direction, value = instruction.split(" ")
        value = int(value)
        if direction == "forward":
            horizon_depth[0] += value
        elif direction == "up":
            horizon_depth[1] -= value
        elif direction == "down":
            horizon_depth[1] += value

    print(f"Multiplication of coordinates: {horizon_depth[0] * horizon_depth[1]}")

    print("#======= Part 2 =======#")

    aim_depth_horizontal = [0, 0, 0]
    for instruction in input_list:
        direction, value = instruction.split(" ")
        value = int(value)
        if direction == "forward":
            aim_depth_horizontal[2] += value
            aim_depth_horizontal[1] += value * aim_depth_horizontal[0]
        elif direction == "up":
            aim_depth_horizontal[0] -= value
        elif direction == "down":
            aim_depth_horizontal[0] += value

    print(f"Multiplication of coordinates: {aim_depth_horizontal[1] * aim_depth_horizontal[2]}")
