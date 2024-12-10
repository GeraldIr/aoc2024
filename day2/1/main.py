def main():
    with open("input") as f:
        lines = f.read().splitlines()

    reports = [[int(v) for v in line.split(" ")] for line in lines]

    count = 0

    for report in reports:

        if not (sorted(report) == report or list(reversed(sorted(report))) == report):
            continue

        shifted_report = report.copy()
        report.pop(-1)
        shifted_report.pop(0)

        if any(
            abs(cur - nex) > 3 or cur == nex for cur, nex in zip(report, shifted_report)
        ):
            continue

        count += 1

    print(count)


if __name__ == "__main__":
    main()
