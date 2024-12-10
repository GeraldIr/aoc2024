import re


def main():
    with open("input", mode="r") as f:
        input = f.read()

    sum = 0

    matches = re.findall(pattern="mul\(\d+,\d+\)", string=input)
    for match in matches:
        factors = str(match).strip("mul()").split(",")
        sum += int(factors[0]) * int(factors[1])

    print(sum)


if __name__ == "__main__":
    main()
