def main():
    with open("input") as f:
        lines = f.readlines()

    list_l = [int(line.split("   ")[0]) for line in lines]
    list_r = [int(line.split("   ")[1].rstrip("\n")) for line in lines]

    sum = 0

    for l in list_l:
        sum += l * list_r.count(l)

    print(sum)


if __name__ == "__main__":
    main()
