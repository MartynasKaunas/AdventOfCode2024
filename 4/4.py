import time

start_time = time.time()

patterns_1 = [
    [(-1, -1), (-2, -2), (-3, -3)], [(0, -1), (0, -2), (0, -3)], [(1, -1), (2, -2), (3, -3)], # Top-left    Top     Top-right
    [(-1, 0), (-2, 0), (-3, 0)],                                 [(1, 0), (2, 0), (3, 0)],    # Left                Right
    [(-1, 1), (-2, 2), (-3, 3)],    [(0, 1), (0, 2), (0, 3)],    [(1, 1), (2, 2), (3, 3)],    # Bottom-left Bottom  Bottom-right            
]
pattern_2 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Top-left, Top-right, Bottom-left, Bottom-right

data = {}
count1 = 0
count2 = 0

for i, line in enumerate(open("adventofcode2024/4/4.txt", 'r'), 0):
    for j, value in enumerate(line.strip(), 0):
        data[(j, i)] = value

for (x, y), value in data.items():
    if value == 'X':
        for direction in patterns_1:
            positions = [(x + dx, y + dy) for dx, dy in direction]

            if all(pos in data for pos in positions):
                values = [data[pos] for pos in positions]

                if values == ['M', 'A', 'S']:
                    count1 += 1

    if value == 'A':
        corners = [data.get((x + dx, y + dy)) for dx, dy in pattern_2]

        if len(corners) == 4 and corners.count('M') == 2 and corners.count('S') == 2:
            pairs = [(corners[0], corners[3]), (corners[1], corners[2])]
            valid_pairs = {('M', 'S'), ('S', 'M')}
            
            if tuple(pairs[0]) in valid_pairs and tuple(pairs[1]) in valid_pairs:
                count2 += 1

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Part1: {count1}, Part2: {count2} execution Time: {elapsed_time_ms:.2f} ms")

# 2578 ?
# 1972 ?