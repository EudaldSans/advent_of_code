from collections import namedtuple
from typing import List

Point = namedtuple('Point', 'x y')


def check_engine_gear(points_to_check: List[Point], engine_lines: List[str]) -> bool:
    schematic_height = len(engine_lines)
    schematic_width = len(engine_lines[0])
    for point in points_to_check:
        if point.y >= schematic_height or point.x >= schematic_width: continue
        if point.y < 0 or point.x < 0: continue

        character = engine_lines[point.y][point.x]
        if character.isdigit():
            return True

    return False


def main(file_name: str) -> int:
    with open(file_name, 'r') as engine_file:
        engine_lines = engine_file.readlines()
        engine_lines = [line.strip() for line in engine_lines]

    engine_parts = list()
    for y, line in enumerate(engine_lines):
        new_number = 0
        points_to_check = list()
        for x, character in enumerate(line):
            if character == '*':
                points_to_check.append(Point(x - 1, y - 1))
                points_to_check.append(Point(x - 1, y))
                points_to_check.append(Point(x - 1, y + 1))
                points_to_check.append(Point(x, y - 1))
                points_to_check.append(Point(x, y + 1))
                points_to_check.append(Point(x + 1, y - 1))
                points_to_check.append(Point(x + 1, y))
                points_to_check.append(Point(x + 1, y + 1))

            elif len(points_to_check) > 0:
                if check_engine_gear(points_to_check, engine_lines):
                    engine_parts.append(new_number)

                new_number = 0
                points_to_check.clear()

        if new_number != 0:
            if check_engine_gear(points_to_check, engine_lines):
                engine_parts.append(new_number)

    return sum(engine_parts)


if __name__ == '__main__':
    result = main('schematic.txt')
    print(f'The sum of the engine parts is {result}')

