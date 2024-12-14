import os
import time

class Robot:
    def __init__(self, position, velocity, map_width, map_height):
        self.x, self.y = position
        self.vx, self.vy = velocity
        self.map_width = map_width
        self.map_height = map_height

    def move(self):
        self.x = (self.x + self.vx) % self.map_width
        self.y = (self.y + self.vy) % self.map_height


def create_robots(file, map_width, map_height):
    robots = []
    for line in open(file, 'r').readlines():
        parts = line.split()
        position = tuple(map(int, parts[0][2:].split(",")))
        velocity = tuple(map(int, parts[1][2:].split(",")))
        robot = Robot(position, velocity, map_width, map_height)
        robots.append(robot)
    return robots

def count_quadrants(robots, map_width, map_height):
    q1 = q2 = q3 = q4 = 0
    mid_x = map_width // 2
    mid_y = map_height // 2

    for robot in robots:
        x, y = robot.x, robot.y

        if x == mid_x or y == mid_y:
            continue

        if x > mid_x and y < mid_y:
            q1 += 1
        elif x < mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y > mid_y:
            q3 += 1
        elif x > mid_x and y > mid_y:
            q4 += 1

    return q1, q2, q3, q4

def robots_together(robots, map_width, map_height):
    robot_positions = {(robot.x, robot.y) for robot in robots}
    directions = [
        (-1, -1), (0, -1), (1, -1),
        (-1,  0),          (1,  0),
        (-1,  1), (0,  1), (1,  1)
    ]

    for robot in robots:
        x, y = robot.x, robot.y

        if all(
            (x + dx, y + dy) in robot_positions
            for dx, dy in directions
            if 0 <= x + dx < map_width and 0 <= y + dy < map_height
        ):
            return True

    return False

def draw_map(robots, map_width, map_height, second):
    # os.system('cls' if os.name == 'nt' else 'clear')
    grid = [[0 for _ in range(map_width)] for _ in range(map_height)]

    for robot in robots:
        x, y = robot.x, robot.y
        grid[y][x] += 1

    for row in grid:
        print("".join(str(cell) if cell > 0 else "." for cell in row))
    print(second+1)

class Preset:
    def __init__(self, map_width, map_height, filename, seconds):
        self.map_width = map_width
        self.map_height = map_height
        self.filename = filename
        self.seconds = seconds

if __name__ == "__main__":
    presets = [
        Preset(11, 7, "adventofcode2024/14/test14.txt", 100),
        Preset(101, 103, "adventofcode2024/14/14.txt", 100),
        Preset(101, 103, "adventofcode2024/14/1414.txt", 10000),
    ]

    for preset in presets:
        print(f"Running preset: {preset.filename}")
        map_width = preset.map_width
        map_height = preset.map_height
        seconds = preset.seconds
        file = preset.filename

        robots = create_robots(file, map_width, map_height)

        for i in range(seconds):
            for robot in robots:
                robot.move()

            if robots_together(robots, map_width, map_height) == True:
                draw_map(robots, map_width, map_height, i)
                time.sleep(5)

        q1, q2, q3, q4 = count_quadrants(robots, map_width, map_height)
        safety_factor = q1 * q2 * q3 * q4
        print(f"Robots in quadrants: Q1={q1}, Q2={q2}, Q3={q3}, Q4={q4}")
        print(f"Safety Factor: {safety_factor}")
