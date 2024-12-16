def main():
    with open("E:\\home\\aoc2024\\day7\\1\\input", mode="r") as f:
        input = f.read().splitlines()

    possibles = []



    for line in input:
        expected_value, operands = prep_line(line)

        operator_ternary_max = (3**(len(operands) - 1)) - 1
        operator_ternary_padding = len(ternary(operator_ternary_max))

        for operator_alignment in range(operator_ternary_max + 1):
            current_value = operands[0]
            for operand_index, operator in enumerate(ternary(operator_alignment).rjust(operator_ternary_padding, "0")):
                
                if operator == "0":
                    current_value = current_value + operands[operand_index + 1]
                elif operator == "1":
                    current_value = current_value * operands[operand_index + 1]
                else:
                    current_value = int(str(current_value) + str(operands[operand_index + 1]))

            if current_value == expected_value:
                possibles.append(expected_value)
                break

    print(sum(possibles))

    


def prep_line(line):
    return int(line.split(":")[0]), [int(operand) for operand in line.split(" ")[1:]]

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

if __name__ == "__main__":
    main()


