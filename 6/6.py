import os

class Guard:
    def __init__(self, location, state, map):
        self.location = location
        self.state = state
        self.map = map
        self.directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
        self.right_turn = {"^": ">", ">": "v", "v": "<", "<": "^"}

    def move(self):
        x, y = self.location
        dx, dy = self.directions[self.state]
        next_location = (x + dx, y + dy)

        if next_location not in self.map:
            self._mark_visited()
            return False

        if self.map[next_location] == "#":
            self.state = self.right_turn[self.state]
        else:
            self._mark_visited()
            self.location = next_location
        return True

    def _mark_visited(self):
        if self.map[self.location] not in "XL":
            self.map[self.location] = "X"

def load_map(file):
    rows = open(file, 'r').readlines()
    map = {}
    initial_location = None
    for y, row in enumerate(rows):
        for x, char in enumerate(row.strip()):
            map[(x, y)] = char
            if char == "^":
                initial_location = (x,y)
    return map, initial_location, rows

def detect_loop(location, initial_map, start_location):
    test_map = initial_map.copy()
    test_map[location] = "#"
    test_guard = Guard(start_location, "^", test_map)
    visited = set()

    while True:
        if (test_guard.location, test_guard.state) in visited:
            return True
        visited.add((test_guard.location, test_guard.state))
        if not test_guard.move():
            return False
        
def print_map(map, rows, guard=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(len(rows)):
        for x in range(len(rows[y].strip())):
            if guard and (x, y) == guard.location:
                print(guard.state, end="")
            else:
                print(map.get((x, y), " "), end="")
        print()

def main():
    initial_map, initial_location, rows = load_map("adventofcode2024/6/6.txt")
    guard = Guard(initial_location, "^", initial_map)
    visited_locations = set()

    while guard.move():
        visited_locations.add(guard.location)
        if guard.map.get(guard.location) not in "XL":
            if detect_loop(guard.location, initial_map, initial_location):
                guard.map[guard.location] = "L"
        # print_map(guard.map, rows, guard)
        # time.sleep(0.05)

    # print_map(guard.map, rows)
    visited_count = sum(1 for value in guard.map.values() if value in "XL")
    loop_count = sum(1 for value in guard.map.values() if value == "L")
    print(f"Locations visited: {visited_count}")
    print(f"Loop-causing locations: {loop_count}")

if __name__ == "__main__":
    main()

# 4647
# 1723