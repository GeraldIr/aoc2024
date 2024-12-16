
# up, right, down, left
dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

def main():

    with open("E:\\home\\aoc2024\\day6\\1\\input", mode="r") as f:
        map = f.read().splitlines()

    current_dir = 0
    current_pos = [(map.index(line), line.index("^")) for line in map if "^" in line][0]
    locations = [current_pos]

    while True:
        # Look Ahead
        next_square = check_ahead(current_pos, current_dir, map)

        if next_square == False:
            break
        # Obstacle
        if next_square == "#":
            current_dir = get_next_dir(current_dir)

        current_pos = (current_pos[0] + dirs[current_dir][0], current_pos[1] + dirs[current_dir][1])

        locations.append(current_pos)
        # No Obstacle
    
    print(len(set(locations)))


def check_ahead(position, direction, map):
    next_pos = (position[0] + dirs[direction][0], position[1] + dirs[direction][1])


    if (next_pos[0] * next_pos[1]) < 0:
        return False
    
    try:
        return map[next_pos[0]][next_pos[1]]
    except IndexError as e:
        return False

def get_next_dir(current_direction):
    return (current_direction + 1) % 4

if __name__  == "__main__":
    main()