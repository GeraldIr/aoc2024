import math

def main():
    with open("E:\\home\\aoc2024\\day9\\1\\input", mode="r") as f:
        input = f.read()
    
    file = construct_file(input)

    defragmented_file = defragment_file(file)
    print(checksum(defragmented_file))

    
def construct_file(input):
    file = []
    for i in range(math.ceil(len(input)/2)):

        file_length = int(input[i*2])  
        whitespace_length = 0 if len(input) <= (i*2)+1 else int(input[(i*2)+1])

        file.append([i] * file_length)
        file.append([None] * whitespace_length)

    return [x for xs in file for x in xs] # Flatten

def defragment_file(file: list):
    while None in file:
        to_insert = file.pop()
        if None in file:
            file[file.index(None)] = to_insert

    return file

def checksum(file: list):
    return sum([i * v for i, v in enumerate(file)])


if __name__ == "__main__":
    main()