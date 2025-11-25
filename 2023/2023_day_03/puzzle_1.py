from collections import namedtuple
from typing import List

import math

Point = namedtuple('Point', 'x y')


class EnginePart:
    def __init__(self, part_id: int, start_pos: Point) -> None:
        self.id = part_id
        self.start = start_pos
        self.length = int(math.log10(part_id))+1

    def __mul__(self, other: 'EnginePart') -> int:
        return self.id * other.id

    def __repr__(self) -> str:
        return f'Engine Part ID: {self.id}, located at ({self.start.x}, {self.start.y})'

    def is_point_adjacent_to_part(self, point: Point) -> bool:
        if point.y < self.start.y - 1:              return False
        if point.y > self.start.y + 1:              return False
        if point.x < self.start.x - 1:              return False
        if point.x > self.start.x + self.length:    return False

        return True


def check_engine_part(points_to_check: List[Point], engine_lines: List[str]) -> bool:
    schematic_height = len(engine_lines)
    schematic_width = len(engine_lines[0])
    for point in points_to_check:
        if point.y >= schematic_height or point.x >= schematic_width: continue
        if point.y < 0 or point.x < 0: continue

        character = engine_lines[point.y][point.x]
        if character != '.':
            return True

    return False


def main(file_name: str) -> int:
    with open(file_name, 'r') as engine_file:
        engine_lines = engine_file.readlines()
        engine_lines = [line.strip() for line in engine_lines]

    engine_parts = list()
    for y, line in enumerate(engine_lines):
        part_start = None
        new_number = 0
        points_to_check = list()
        for x, character in enumerate(line):
            if character.isdigit():
                if new_number == 0:
                    part_start = Point(x, y)
                    points_to_check.append(Point(x - 1, y - 1))
                    points_to_check.append(Point(x - 1, y))
                    points_to_check.append(Point(x - 1, y + 1))

                new_number = new_number * 10 + int(character)

                points_to_check.append(Point(x, y - 1))
                points_to_check.append(Point(x, y + 1))

            elif new_number != 0:
                points_to_check.append(Point(x, y - 1))
                points_to_check.append(Point(x, y))
                points_to_check.append(Point(x, y + 1))

                if check_engine_part(points_to_check, engine_lines):
                    engine_parts.append(EnginePart(new_number, part_start))

                new_number = 0
                points_to_check.clear()

        if new_number != 0:
            if check_engine_part(points_to_check, engine_lines):
                engine_parts.append(EnginePart(new_number, part_start))

    engin_ids = [part.id for part in engine_parts]
    print(f'The sum of the engine parts is {sum(engin_ids)}')

    gear_ratios = list()
    for y, line in enumerate(engine_lines):
        for x, character in enumerate(line):
            if character != '*': continue

            gear_position = Point(x, y)

            adjacent_engine_parts = [engine_part for engine_part in engine_parts
                                     if engine_part.is_point_adjacent_to_part(gear_position)]

            if len(adjacent_engine_parts) < 2: continue
            if len(adjacent_engine_parts) > 2: continue

            gear_ratio = adjacent_engine_parts[0] * adjacent_engine_parts[1]
            gear_ratios.append(gear_ratio)

            print(adjacent_engine_parts)

    print(f'The sum of gear ratios is {sum(gear_ratios)}')


if __name__ == '__main__':
    result = main('schematic.txt')


