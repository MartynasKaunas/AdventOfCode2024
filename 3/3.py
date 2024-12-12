import re
import time

start_time = time.time()

part = 2
enabled = True
total_sum = 0
input = open("adventofcode2024/3/3.txt", 'r').read()

for segment in re.split(r"(do\(\)|don't\(\))", input):
    if part == 2:
        enabled = {"do()": True, "don't()": False}.get(segment, enabled)
    if enabled:
        total_sum += sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", segment))


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Total Sum: {total_sum}, part {part} execution Time: {elapsed_time_ms:.2f} ms")