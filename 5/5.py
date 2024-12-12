import random

sum_of_middles_1 = 0
sum_of_middles_2 = 0
valid_updates = []
invalid_updates = []

inputs = open("adventofcode2024/5/5.txt", 'r').read().split("\n\n")

rules = [tuple(map(int, line.split('|'))) for line in inputs[0].split("\n")]
updates = [list(map(int, line.split(','))) for line in inputs[1].split("\n")]

def validate_update(update):
    for page in update:
        if page in {rule[0] for rule in rules}:
            relevant_rules = [rule for rule in rules if rule[0] == page and rule[1] in update]

            for rule in relevant_rules:
                first, second = rule
                if update.index(first) > update.index(second):
                    return False
    return True

def fix_update(update, rules):
    update_set = set(update)
    relevant_rules = [rule for rule in rules if rule[0] in update_set and rule[1] in update_set]

    fixed = False
    while not fixed:
        fixed = True
        for i in range(len(update) - 1):
            first, second = update[i], update[i + 1]
            if (first, second) not in relevant_rules and (second, first) in relevant_rules:
                update[i], update[i + 1] = update[i + 1], update[i]
                fixed = False
    return update

fixed_updates = []
for update in updates:
    if validate_update(update):
        valid_updates.append(update)
    else:
        fixed_update = fix_update(update, rules)
        fixed_updates.append(fixed_update)

sum_of_middles_1 = sum(update[len(update) // 2] for update in valid_updates)
sum_of_middles_2 = sum(update[len(update) // 2] for update in fixed_updates)
print(f"Part 1: {sum_of_middles_1}, Part 2: {sum_of_middles_2}")

# 3608
# 4922
