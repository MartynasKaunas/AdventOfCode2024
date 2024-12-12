# sum of the numbers of 9 positions reachable from each zero
# sum of the numbers of possible trails from each zero

part = 2
grid = {}
with open('adventofcode2024/10/10.txt') as file:
    for y, row in enumerate(file):
        for x, char in enumerate(row.strip()):
            grid[(x, y)] = int(char)

def search(pos, seen, height=0):
    if pos in grid and grid[pos] == height:
        if height < 9 or part == 1 and pos in seen:
            neighbors = [(pos[0] + dx, pos[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
            return sum(search(neighbor, seen, height + 1) for neighbor in neighbors)
        seen.add(pos)
        return 1
    return 0

print(sum(search(pos, set()) for pos in grid if grid[pos] == 0))


# 517
# 1116