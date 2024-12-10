def main():
    with open("input") as f:
        lines = f.read().splitlines()

    reports = [[int(v) for v in line.split(" ")] for line in lines]

    count = 0

    for report in reports:
        for i in range(len(report)):
            dampened_report = report.copy()
            dampened_report.pop(i)
            if check_safety(dampened_report) == -1:
                count += 1
                break

    print(count)


def check_safety(input):
    # Monotone

    # Level Distance
    for k in range(len(input) - 1):
        if abs(input[k] - input[k + 1]) > 3:
            return k + 1

    # Increasing
    for i in range(len(input) - 1):
        if not input[i] < input[i + 1]:
            fail_i = i
            break
    else:
        fail_i = -1

    # Decreasing
    for j in range(len(input) - 1):
        if not input[j] > input[j + 1]:
            fail_j = j
            break
    else:
        fail_j = -1

    if fail_i != -1 and fail_j != -1:
        return max(fail_i, fail_j)

    return -1


if __name__ == "__main__":
    main()
