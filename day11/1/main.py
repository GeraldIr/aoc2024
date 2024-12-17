import itertools
import threading

from collections import Counter

def main():
    with open("E:\\home\\aoc2024\\day11\\1\\input", mode="r") as f:
        input = [int(v) for v in f.read().splitlines()[0].split(" ")]

        stones = iterate_stones(input, 25)
        

        print(sum(stones.values()))



def apply_rules(stones):
    new_stones = Counter()
    for stone_id, amount in stones:
        if stone_id == 0:
            new_stones[1] += amount
        elif len(str(stone_id)) % 2 == 0:
            x = int(str(stone_id)[: int(len(str(stone_id)) / 2)])
            y = int(str(stone_id)[int(len(str(stone_id)) / 2) :].lstrip("0") or 0)
            new_stones[x] += amount
            new_stones[y] += amount
        else:
            new_stones[stone_id * 2024] += amount

    return new_stones


def iterate_stones(stones, iterations):
    stones = Counter(stones)
    for i in range(iterations):
        stones = apply_rules(stones.items())
        print(i)

    return stones

def flatmap(func, *iterable):
    return Counter(itertools.chain.from_iterable(map(func, *iterable)))



if __name__ == "__main__":
    main()
