from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(grid, start_x, start_y, visited, rows, cols):
    letter, queue, region = grid[start_x][start_y], deque([(start_x, start_y)]), []
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        region.append((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == letter:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return region

def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = []

    for x in range(rows):
        for y in range(cols):
            if not visited[x][y]:
                regions.append(bfs(grid, x, y, visited, rows, cols))

    return regions


def calculate_edges(grid, region):
    rows = len(grid)
    cols = len(grid[0])
    edges = []
    horizontal_edges = []
    vertical_edges = []

    for y, x in region:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < cols and 0 <= ny < rows) or grid[ny][nx] != grid[y][x]:
                if dx != 0:  # Vertical edge
                    edge = (y, (x, nx))
                    vertical_edges.append(edge)
                if dy != 0:  # Horizontal edge
                    edge = (x, (y, ny))
                    horizontal_edges.append(edge)
                
                edges.append(edge) # Part 1 result

    count = get_continuous_edges(group_edges_by_alignment(horizontal_edges)) + \
            get_continuous_edges(group_edges_by_alignment(vertical_edges))

    # print(f"Region: {region}, Sub-edges: {edges}, Edges: {count}")
    return count


# (0, (1, 0))
# (1, (1, 0))
# (2, (1, 0))       (1, 0): [0, 1, 2]
# (0, (4, 5))  =>   (4, 5): [0]
# (1, (5, 6))       (5, 6): [1, 2]
# (2, (5, 6))
def group_edges_by_alignment(edge_list):
    grouped_edges = {}
    for alignment, between in edge_list:
        if between not in grouped_edges:
            grouped_edges[between] = []
        grouped_edges[between].append(alignment)

    return grouped_edges

# ((0,0): [1,2, 5,6,7, 9]) => 3
def get_continuous_edges(grouped_edges):
    total_edges = 0

    for indices in grouped_edges.values():
        indices.sort()
        edge_count = 1
        
        for i in range(1, len(indices)):
            if indices[i] != indices[i - 1] + 1:
                edge_count += 1
        total_edges += edge_count
    
    return total_edges


grid = [list(line.strip()) for line in open("adventofcode2024/12/12.txt", 'r').readlines()]
regions = find_regions(grid)
total_price = sum(len(region) * calculate_edges(grid, region) for region in regions)

print(f"Total fence price: {total_price}")

# 1546338
# 978590
