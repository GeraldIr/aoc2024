
# up, right, down, left
dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

def main():

    with open("E:\\home\\aoc2024\\day6\\2\\input", mode="r") as f:
        map = f.read().splitlines()

    _, obstacle_locations = run_sim(map=map)


    obstacle_locations = list(set([l[0] for l in obstacle_locations]))
    outcomes = []
    for i, obstacle_location in enumerate(obstacle_locations):
        simulation_map = map.copy()
        line = list(simulation_map[obstacle_location[0]])
        if line[obstacle_location[1]] == "^":
            continue
        line[obstacle_location[1]] = "#"
        simulation_map[obstacle_location[0]] = "".join(line)
        if run_sim(simulation_map)[0]:
            outcomes.append(obstacle_location)
        print(i)
    
    print(len(outcomes))

def run_sim(map):
    current_dir = 0
    current_pos = [(map.index(line), line.index("^")) for line in map if "^" in line][0]
    location_directions = [(current_pos, current_dir)]

    while True:
        # Look Ahead
        
        next_square = check_ahead(current_pos, current_dir, map)

        if next_square == False:
            break
        # Obstacle
        if next_square == "#":
            current_dir = get_next_dir(current_dir)

        # Literal Corner Case
        if check_ahead(current_pos, current_dir, map) == "#":
            current_dir = get_next_dir(current_dir)

        current_pos = (current_pos[0] + dirs[current_dir][0], current_pos[1] + dirs[current_dir][1])

        # LOOP
        if (current_pos, current_dir) in location_directions:
            return True, location_directions

        location_directions.append((current_pos, current_dir))
        # No Obstacle
    # NO LOOP, TERMINATES OFF MAP
    return False, location_directions


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