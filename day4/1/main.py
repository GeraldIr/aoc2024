filter_horizontal_right = {(0, 0): "X", (0, 1): "M", (0, 2): "A", (0, 3): "S"}
filter_horizontal_left = {(0, 0): "X", (0, -1): "M", (0, -2): "A", (0, -3): "S"}
filter_vertical_down = {(0, 0): "X", (1, 0): "M", (2, 0): "A", (3, 0): "S"}
filter_vertical_up = {(0, 0): "X", (-1, 0): "M", (-2, 0): "A", (-3, 0): "S"}

filter_diagonal_down_left = {(0, 0): "X", (1, -1): "M", (2, -2): "A", (3, -3): "S"}
filter_diagonal_down_right = {(0, 0): "X", (1, 1): "M", (2, 2): "A", (3, 3): "S"}
filter_diagonal_up_left = {(0, 0): "X", (-1, -1): "M", (-2, -2): "A", (-3, -3): "S"}
filter_diagonal_up_right = {(0, 0): "X", (-1, 1): "M", (-2, 2): "A", (-3, 3): "S"}


def main():
    with open("/home/gerald/co/aoc2024/day4/1/input", mode="r") as f:
        input = f.read().splitlines()

    xmas_count = 0

    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] == "X":
                xmas_count += [
                    apply_filter(
                        input=input, coordinates=(x, y), filter=filter_horizontal_right
                    ),
                    apply_filter(
                        input=input, coordinates=(x, y), filter=filter_horizontal_left
                    ),
                    apply_filter(
                        input=input, coordinates=(x, y), filter=filter_vertical_down
                    ),
                    apply_filter(
                        input=input, coordinates=(x, y), filter=filter_vertical_up
                    ),
                    apply_filter(
                        input=input,
                        coordinates=(x, y),
                        filter=filter_diagonal_down_left,
                    ),
                    apply_filter(
                        input=input,
                        coordinates=(x, y),
                        filter=filter_diagonal_down_right,
                    ),
                    apply_filter(
                        input=input, coordinates=(x, y), filter=filter_diagonal_up_left
                    ),
                    apply_filter(
                        input=input, coordinates=(x, y), filter=filter_diagonal_up_right
                    ),
                ].count(True)

    print(xmas_count)


def apply_filter(input, coordinates, filter: dict):
    try:
        return all(
            [
                input[coordinates[0] + offset[0]][coordinates[1] + offset[1]] == letter
                and coordinates[0] + offset[0] >= 0
                and coordinates[1] + offset[1] >= 0
                for offset, letter in filter.items()
            ]
        )

    except:
        return False


if __name__ == "__main__":
    main()
