from collections import namedtuple
from typing import List

import numpy as np

Point = namedtuple('Point', ('x', 'y'))


class Cable:
    GRID_SIZE = 5000

    def __init__(self):
        self.head = Point((self.GRID_SIZE//2), self.GRID_SIZE//2)
        self.trail = np.zeros((self.GRID_SIZE, self.GRID_SIZE))

    def add_step(self, order: str):
        direction = order[0]
        step_length = int(order[1:])

        x = self.head.x
        y = self.head.y

        if direction == 'U':
            self.head = Point(x, y + step_length)

            if x >= self.GRID_SIZE or x < 0:
                return
            if y < 0 and y + step_length >= self.GRID_SIZE:
                self.trail[x, :] = 1
                return
            if y < 0:
                self.trail[x, : y + step_length + 1] = 1
                return
            if y + step_length >= self.GRID_SIZE:
                self.trail[x, y:] = 1
                return

            self.trail[x, y: y + step_length + 1] = 1

        if direction == 'D':
            self.head = Point(x, y - step_length)

            if x >= self.GRID_SIZE or x < 0:
                return
            if y - step_length < 0 and y >= self.GRID_SIZE:
                self.trail[x, :] = 1
                return
            if y - step_length < 0:
                self.trail[x, : y] = 1
                return
            if y >= self.GRID_SIZE:
                self.trail[x, y - step_length:] = 1
                return

            self.trail[x, y - step_length: y] = 1

        if direction == 'R':
            self.head = Point(x + step_length, y)

            if y >= self.GRID_SIZE or y < 0:
                return
            if x < 0 and x + step_length >= self.GRID_SIZE:
                self.trail[:, y] = 1
                return
            if x < 0:
                self.trail[: x + step_length + 1, : y] = 1
                return
            if x + step_length >= self.GRID_SIZE:
                self.trail[x:, y] = 1
                return

            self.trail[x: x + step_length + 1, y] = 1

        if direction == 'L':
            self.head = Point(x - step_length, y)

            if y >= self.GRID_SIZE or y < 0:
                return
            if x - step_length < 0 and x >= self.GRID_SIZE:
                self.trail[:, y] = 1
                return
            if x - step_length < 0:
                self.trail[: x, y] = 1
                return
            if x >= self.GRID_SIZE:
                self.trail[x - step_length:, y] = 1
                return

            self.trail[x - step_length: x, y] = 1

    def trace_cable(self, cable_info: str):
        for order in cable_info.split(','):
            self.add_step(order)

    def __str__(self) -> str:
        return str(self.trail)

    @property
    def starting_point(self):
        return Point(self.GRID_SIZE//2, self.GRID_SIZE//2)


def manhattan_distance(point_1: Point, point_2: Point) -> int:
    return abs(point_1.x - point_2.x) + abs(point_1.y - point_2.y)


if __name__ == '__main__':
    cable_1 = Cable()
    cable_2 = Cable()

    with open('circuit.txt') as file:
        cable_1.trace_cable(file.readline().rstrip())
        cable_2.trace_cable(file.readline().rstrip())

    result = cable_1.trail * cable_2.trail
    intersections = np.argwhere(result == 1)
    intersections = [Point(x, y) for (x, y) in intersections]

    final_distance = cable_1.GRID_SIZE*2
    starting_point = cable_1.starting_point

    for intersection in intersections:
        if intersection == starting_point:
            continue

        if manhattan_distance(starting_point, intersection) < final_distance:
            final_distance = manhattan_distance(starting_point, intersection)

    print(f'The final manhattan distance is: {final_distance}')
