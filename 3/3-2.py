from re import split, findall

total_sum = 0
enabled = True
part = 2
input = open("adventofcode2024/3/3.txt", "r").read()

for segment in split(r"(do\(\)|don't\(\))", input):
    if part == 2:
        enabled = {"do()": True, "don't()": False}.get(segment, enabled)
    if enabled:
        total_sum += sum(int(x) * int(y) for x, y in findall(r"mul\((\d+),(\d+)\)", segment))

print("Sum of mults:", total_sum)