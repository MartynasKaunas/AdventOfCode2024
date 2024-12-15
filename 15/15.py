import os
import time

class Robot:
    def __init__(self, position, map_data, move_list):
        self.position = position
        self.map = map_data
        self.move_list = move_list
        self.directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        self.steps = 0

    def is_within_bounds(self, x, y):
        return 0 <= x < self.cols and 0 <= y < self.rows

    def move(self):
        if self.steps >= len(self.move_list):
            return

        direction = self.move_list[self.steps]
        dx, dy = self.directions[direction]

        next_x = self.position[0] + dx
        next_y = self.position[1] + dy

        if not self.is_within_bounds(next_x, next_y):
            return

        next_cell = self.map[next_y][next_x]

        if next_cell == "#":
            pass
        elif next_cell == ".":
            self.update_robot_position(next_x, next_y)
        elif next_cell in "[]":
            if direction in "^v":
                self.push_boxes_up_down(next_x, next_y, dy)
            else:
                self.push_boxes_left_right(next_x, next_y, dx)
        elif next_cell == "O":
            self.push_boxes(next_x, next_y, dx, dy)

        self.steps += 1

    def push_boxes_left_right(self, start_x, start_y, dx):
        box_positions = []

        x, y = start_x, start_y

        while self.is_within_bounds(x, y) and self.map[y][x] in "[]":
            if self.map[y][x] == "[":
                box_positions.append(((x, y), (x+1, y)))
                x+=2
            elif self.map[y][x] == "]":
                box_positions.append(((x, y), (x-1, y)))
                x-=2

        if self.is_within_bounds(x, y) and self.map[y][x] == ".":        
            for (xl, yl), (xr, yr) in reversed(box_positions):
                self.map[yl][xl + dx] = "]" if dx == -1 else "["
                self.map[yr][xr + dx] = "[" if dx == -1 else "]"

            self.update_robot_position(start_x, start_y)

    def push_boxes_up_down(self, start_x, start_y, dy):
        box_positions = set()

        def detect_boxes(x, y, dy):
            if not self.is_within_bounds(x, y):
                return False

            if self.map[y][x] == "#":
                return False

            if self.map[y][x] == "[":
                box_tuple = tuple(sorted(((x, y), (x + 1, y))))
                if box_tuple not in box_positions:
                    box_positions.add(box_tuple)
                    if not detect_boxes(x, y + dy, dy) or not detect_boxes(x + 1, y + dy, dy):
                        return False

            elif self.map[y][x] == "]":
                box_tuple = tuple(sorted(((x, y), (x - 1, y))))
                if box_tuple not in box_positions:
                    box_positions.add(box_tuple)
                    if not detect_boxes(x, y + dy, dy) or not detect_boxes(x - 1, y + dy, dy):
                        return False

            return True

        if self.is_within_bounds(start_x, start_y) and self.map[start_y][start_x] in "[]":
            if not detect_boxes(start_x, start_y, dy):
                return

        for (xl, yl), (xr, yr) in sorted(box_positions, key=lambda box: min(box[0][1], box[1][1]), reverse=(dy == 1)):
            self.map[yl + dy][xl] = "["
            self.map[yl][xl] = '.'
            self.map[yr + dy][xr] = "]"
            self.map[yr][xr] = '.'
                
        self.update_robot_position(start_x, start_y)

    # Part 1
    def push_boxes(self, start_x, start_y, dx, dy):
        box_positions = []
        x, y = start_x, start_y

        while self.is_within_bounds(x, y) and self.map[y][x] == "O":
            box_positions.append((x, y))
            x += dx
            y += dy

        if self.is_within_bounds(x, y) and self.map[y][x] == ".":
            for bx, by in reversed(box_positions):
                self.map[by + dy][bx + dx] = "O"
                self.map[by][bx] = "."

            self.update_robot_position(start_x, start_y)

    def update_robot_position(self, new_x, new_y):
        old_x, old_y = self.position
        self.map[old_y][old_x] = "."
        self.map[new_y][new_x] = "@"
        self.position = (new_x, new_y)

    def get_gps_sum(self):
        total_sum = 0
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == "[" or cell == "O":
                    total_sum += 100 * y + x
        return total_sum

    def display_map(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n".join("".join(row) for row in self.map))


def read_inputs(file, part):
    with open(file, "r") as file:
        data = file.read().split("\n\n")
        map_data = []
        if part == 1:
            map_data = [list(row) for row in data[0].strip().split("\n")]
        elif part == 2:
            map_data = [list(row.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")) for row in data[0].strip().split("\n")]
        move_list = data[1].replace("\n", "")

        for y, row in enumerate(map_data):
            for x, cell in enumerate(row):
                if cell == "@":
                    return (x, y), map_data, move_list


for part in [1,2]:
    robot_position, map_data, move_list = read_inputs("adventofcode2024/15/15.txt", part)
    robot = Robot(robot_position, map_data, move_list)

    for _ in range(len(move_list)):
        robot.move()
        # robot.display_map()
        # time.sleep(0.2)

    # robot.display_map()
    print("GPS Sum:", robot.get_gps_sum())
