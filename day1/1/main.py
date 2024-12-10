def main():
    with open("input") as f:
        lines = f.readlines()

    list_l = [int(line.split("   ")[0]) for line in lines]
    list_r = [int(line.split("   ")[1].rstrip("\n")) for line in lines]

    list_l.sort()
    list_r.sort()

    sum = 0

    for l, r in zip(list_l, list_r):
        sum += abs(l - r)

    print(sum)


if __name__ == "__main__":
    main()
