import math
import sys


def main():
    with open("/home/gerald/co/aoc2024/day9/2/input", mode="r") as f:
        input = f.read()

    constructed_file = construct_file(input)

    sys.setrecursionlimit(21000)  # Standard is 1000 lmao

    defragmented_file = defragment_file(constructed_file)

    print(checksum(defragmented_file))


def construct_file(input):
    file = []
    for i in range(math.ceil(len(input) / 2)):

        file_length = int(input[i * 2])
        whitespace_length = 0 if len(input) <= (i * 2) + 1 else int(input[(i * 2) + 1])

        file.append([i] * file_length)
        file.append([None] * whitespace_length)

    return file  # Flatten


def defragment_file(file: list):
    _, tail = move_one(file, [])
    return flatten(reversed(tail))


def move_one(head, tail):
    if not head:
        return head, tail
    to_move = head.pop()
    if None in to_move or not to_move:
        tail.append(to_move)
        return move_one(head, tail)
    else:
        free_block_index = find_first_free_block(head, len(to_move))
        if not free_block_index:
            tail.append(to_move)
            return move_one(head, tail)
        else:
            head[free_block_index] = insert_into_free_block(
                head[free_block_index], to_move
            )
            tail.append([None] * len(to_move))
            return move_one(head, tail)


def find_first_free_block(file, needed_size):
    for i, block in enumerate(file):
        if block.count(None) >= needed_size:
            return i
    return False


def insert_into_free_block(free_block, to_move):
    return (
        free_block[: len(free_block) - free_block.count(None)]
        + to_move
        + [None] * (free_block.count(None) - len(to_move))
    )


def flatten(to_flatten: list):
    return [x for xs in to_flatten for x in xs]


def checksum(file: list):

    return sum([i * v if v else 0 for i, v in enumerate(file)])


if __name__ == "__main__":
    main()
