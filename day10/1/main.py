def main():
    with open("/home/gerald/co/aoc2024/day10/1/input", mode="r") as f:
        input = f.read().splitlines()

    trailhead_sum = 0

    for x in range(len(input[0])):
        for y in range(len(input)):
            if input[x][y] == "0":
                trailhead_endings = walk_trail(input, x, y)
                trailhead_sum += len(set(trailhead_endings))

    print(trailhead_sum)


def walk_trail(map, x, y):
    starting_tile = map[x][y]
    max_x = len(map[0])
    max_y = len(map)
    if starting_tile == "9":
        return [(x, y)]
    else:
        if check_tile(map, x, y, offset_x=0, offset_y=-1, max_x=max_x, max_y=max_y) == (
            int(starting_tile) + 1
        ):
            trails_up = walk_trail(map, x, y - 1)
        else:
            trails_up = []

        if check_tile(map, x, y, offset_x=1, offset_y=0, max_x=max_x, max_y=max_y) == (
            int(starting_tile) + 1
        ):
            trails_right = walk_trail(map, x + 1, y)
        else:
            trails_right = []

        if check_tile(map, x, y, offset_x=0, offset_y=1, max_x=max_x, max_y=max_y) == (
            int(starting_tile) + 1
        ):
            trails_down = walk_trail(map, x, y + 1)
        else:
            trails_down = []

        if check_tile(map, x, y, offset_x=-1, offset_y=0, max_x=max_x, max_y=max_y) == (
            int(starting_tile) + 1
        ):
            trails_left = walk_trail(map, x - 1, y)
        else:
            trails_left = []

        return trails_up + trails_right + trails_down + trails_left


def check_tile(map, starting_tile_x, starting_tile_y, offset_x, offset_y, max_x, max_y):

    tile_x = starting_tile_x + offset_x
    tile_y = starting_tile_y + offset_y
    if tile_x < 0 or tile_y < 0 or tile_x >= max_x or tile_y >= max_y:
        return 0
    return int(map[tile_x][tile_y])


if __name__ == "__main__":
    main()
