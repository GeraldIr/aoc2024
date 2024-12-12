import math

def main():
    with open("E:\\home\\aoc2024\\day5\\1\\input") as f:
        input = f.read().splitlines()


    rules_to_updates = input.index("")

    rules_input = input[:rules_to_updates]
    updates_input = input[rules_to_updates + 1:]

    rules = {}
    for rule in rules_input:
        k,v = rule.split("|")
        if k in rules:
            rules[k] = [*rules[k], v]
        else:
            rules[k] = [v]


    updates = [update.split(",") for update in updates_input]
    incorrectly_ordered = [update for update in updates if not check_update(list(reversed(update)), rules)]

    reordered = []

    for ic in incorrectly_ordered:
        current = []
        for insert in ic:
            current = insert_correctly(current, insert, rules)

        reordered.append(current)

    sumd = sum([int(co[math.floor(len(co)/2)]) for co in reordered])
    
    print(sumd)

def check_update(inp, rules):
    if len(inp) == 1:
        return True
    
    key = inp[0]
    to_check = inp[1:-1]


    if any([v in rules[key] for v in to_check]):
        return False
    else:
        return check_update(inp[1:], rules)
    
def insert_correctly(current: list, insert, rules):
    if current == []:
        return [insert]
    
    for i in range(len(current)):
        if current[i] in rules[insert]:
            current.insert(i, insert)
            return current
        
    current.append(insert)
    return current



if __name__ == "__main__":
    main()