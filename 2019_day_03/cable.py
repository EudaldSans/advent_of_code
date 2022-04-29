from collections import namedtuple
from typing import List

import numpy as np

Point = namedtuple('Point', ('x', 'y'))


class Cable:
    GRID_SIZE = 5000
    starting_point = Point(GRID_SIZE//2, GRID_SIZE//2)

    def __init__(self, cable_info: str):
        self.head = Point((self.GRID_SIZE//2), self.GRID_SIZE//2)
        self.trail = np.zeros((self.GRID_SIZE, self.GRID_SIZE))

        self.cable_info = cable_info

        for order in cable_info.split(','):
            self.add_step(order, True)

    def update_trail(self, old_pos: Point, new_pos: Point):
        x_min = min(old_pos.x, new_pos.x)
        x_max = max(old_pos.x, new_pos.x)

        if x_max >= self.GRID_SIZE:
            x_max = self.GRID_SIZE - 1
        if x_min < 0:
            x_min = 0

        y_min = min(old_pos.y, new_pos.y)
        y_max = max(old_pos.y, new_pos.y)

        if y_max >= self.GRID_SIZE:
            y_max = self.GRID_SIZE - 1
        if y_min < 0:
            y_min = 0

        self.trail[x_min: x_max + 1, y_min: y_max + 1] = 1

    def add_step(self, order: str, update_trail: bool):
        direction = order[0]
        step_length = int(order[1:])

        x = self.head.x
        y = self.head.y

        if direction == 'U':
            self.head = Point(x, y + step_length)

        if direction == 'D':
            self.head = Point(x, y - step_length)

        if direction == 'R':
            self.head = Point(x + step_length, y)

        if direction == 'L':
            self.head = Point(x - step_length, y)

        if update_trail:
            self.update_trail(Point(x, y), self.head)

    def __str__(self) -> str:
        return str(self.trail)

    def steps_to_point(self, point: Point):
        pass

    @classmethod
    def manhattan_distance(cls, point: Point):
        return abs(cls.starting_point.x - point.x) + abs(cls.starting_point.y - point.y)

    def steps_to_point(self, point):
        self.head = self.starting_point

        for order in self.cable_info.split(','):
            direction = order[0]
            step_length = int(order[1:])

            x = self.head.x
            y = self.head.y

            if direction == 'U':
                self.head = Point(x, y + step_length)

            if direction == 'D':
                self.head = Point(x, y - step_length)

            if direction == 'R':
                self.head = Point(x + step_length, y)

            if direction == 'L':
                self.head = Point(x - step_length, y)


def find_intersections(cable_1: Cable, cable_2: Cable) -> List[Point]:
    result = cable_1.trail * cable_2.trail
    intersections = np.argwhere(result == 1)
    intersections = [Point(x, y) for (x, y) in intersections]

    return intersections
