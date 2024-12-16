def main():
    with open("E:\\home\\aoc2024\\day7\\1\\input", mode="r") as f:
        input = f.read().splitlines()

    possibles = []



    for line in input:
        expected_value, operands = prep_line(line)

        operator_binary_max = (2**(len(operands) - 1)) - 1
        operator_binary_padding = len(bin(operator_binary_max)[2:])

        for operator_alignment in range(operator_binary_max + 1):
            current_value = operands[0]
            for operand_index, operator in enumerate(bin(operator_alignment)[2:].rjust(operator_binary_padding, "0")):
                current_value = current_value * operands[operand_index + 1] if operator == "1" else current_value + operands[operand_index + 1]

            if current_value == expected_value:
                possibles.append(expected_value)
                break

    print(sum(possibles))

    


def prep_line(line):
    return int(line.split(":")[0]), [int(operand) for operand in line.split(" ")[1:]]

if __name__ == "__main__":
    main()