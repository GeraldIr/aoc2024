import threading


def main():
    with open("/home/gerald/co/aoc2024/day11/1/input", mode="r") as f:
        input = [int(v) for v in f.read().splitlines()[0].split(" ")]

        print(len(iterate_stones(input, 25)))


def apply_rules(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        x = int(str(stone)[: int(len(str(stone)) / 2)])
        y = int(str(stone)[int(len(str(stone)) / 2) :].strip("0") or 0)
        return [x, y]
    else:
        return [stone * 2024]


def iterate_stones(stones, iterations):
    for i in range(iterations):
        new_stones = []
        for stone in stones:
            new_stones = new_stones + apply_rules(stone)
        stones = new_stones
    return stones


if __name__ == "__main__":
    main()
