import itertools

def main():
    with open("E:\\home\\aoc2024\\day8\\2\\input", mode="r") as f:
        input = f.read().splitlines()

    symbol_coordinates = {}

    max_x = len(input[0]) - 1
    max_y = len(input) - 1
    
    for x, line in enumerate(input):
        for y, v in enumerate(line):
            if v == ".":
                continue
            if v in symbol_coordinates:
                symbol_coordinates[v].append((x,y))
            else:
                symbol_coordinates[v] = [(x,y)]


    antinodes = []

    # Finding Antinodes
    for symbol in symbol_coordinates.keys():
        for pair in itertools.combinations(symbol_coordinates[symbol], 2):
            signal_1 = pair[0]
            signal_2 = pair[1]

            delta = (signal_2[0] - signal_1[0], signal_2[1] - signal_1[1])

            for repeat in range(0, max(max_y, max_x)):
                antinode_1 = (signal_1[0] - (delta[0] * repeat), signal_1[1] - (delta[1] * repeat))
                antinode_2 = (signal_2[0] + (delta[0] * repeat), signal_2[1] + (delta[1] * repeat))

                antinodes.append(antinode_1)
                antinodes.append(antinode_2)

    # Filtering Antinodes

    antinodes = list(set(antinodes)) # No Dupes



    antinodes = [antinode for antinode in antinodes if check_bounds(coordinates=antinode, max_x=max_x, max_y=max_y)]
    
    print(len(antinodes))


def check_bounds(coordinates, max_x, max_y):
    return coordinates[0] >= 0 and coordinates[1] >= 0 and coordinates[0] <= max_x and coordinates[1] <= max_y


if __name__ == "__main__":
    main()