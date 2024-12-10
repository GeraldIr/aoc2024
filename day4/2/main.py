filter_MM = {(0, 0): "A", (-1, -1): "M", (1, 1): "S", (1, -1): "M", (-1, 1): "S"}
filter_MS = {(0, 0): "A", (-1, -1): "M", (1, 1): "S", (1, -1): "S", (-1, 1): "M"}
filter_SM = {(0, 0): "A", (-1, -1): "S", (1, 1): "M", (1, -1): "M", (-1, 1): "S"}
filter_SS = {(0, 0): "A", (-1, -1): "S", (1, 1): "M", (1, -1): "S", (-1, 1): "M"}


def main():
    with open("/home/gerald/co/aoc2024/day4/2/input", mode="r") as f:
        input = f.read().splitlines()

    xmas_count = 0

    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] == "A":
                xmas_count += [
                    apply_filter(input=input, coordinates=(x, y), filter=filter_MM),
                    apply_filter(input=input, coordinates=(x, y), filter=filter_MS),
                    apply_filter(input=input, coordinates=(x, y), filter=filter_SM),
                    apply_filter(input=input, coordinates=(x, y), filter=filter_SS),
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
