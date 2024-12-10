import re


def main():
    with open("/home/gerald/co/aoc2024/day3/2/input", mode="r") as f:
        lines = f.read().splitlines()

    input = ""

    for line in lines:
        input += line

    input = "do()" + input

    input_filtered = re.findall(
        pattern="(?:do\(\).*?)+(?:(?:don't\(\))|$)", string=input
    )

    sum = 0

    for finp in input_filtered:
        matches = re.findall(pattern="mul\(\d+,\d+\)", string=finp)
        for match in matches:
            factors = str(match).strip("mul()").split(",")
            sum += int(factors[0]) * int(factors[1])

    print(sum)


if __name__ == "__main__":
    main()
