import string

symbols = list(string.ascii_letters + string.digits)
antennas = {symbol: [] for symbol in symbols}
antinodes = set()
max_x = max_y = 0
map = {}

for y, row in enumerate(open("adventofcode2024/8/8.txt", 'r').readlines()):
    for x, char in enumerate(row.strip()):
        map[(x, y)] = char
        if char in symbols:
            antennas[char].append((x, y))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

def place_antinodes(start_point, dx, dy):
    current_x, current_y = start_point
    while 0 <= current_x <= max_x and 0 <= current_y <= max_y:
        if (current_x, current_y) not in {start_point}:
            antinodes.add((current_x, current_y))
        current_x += dx
        current_y += dy

for locations in antennas.values():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            point1, point2 = locations[i], locations[j]
            dx, dy = point2[0] - point1[0], point2[1] - point1[1]
            place_antinodes(point1, dx, dy)
            place_antinodes(point2, -dx, -dy)

antinode_count = 0
for y in range(max_y + 1):
    for x in range(max_x + 1):
        char = map.get((x, y), '.')
        if (char in symbols and len(antennas[char]) > 1) or ((x, y) in antinodes):
            char = '#'
        if char == '#':
            antinode_count += 1
        print(char, end="")
    print()
print(f"Antinode count: {antinode_count}")
