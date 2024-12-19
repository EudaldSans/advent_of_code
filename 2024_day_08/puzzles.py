import math
from collections import namedtuple
from copy import deepcopy
from typing import List
import itertools

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['a', 'b', 'c'])
Antenna = namedtuple('Antenna', ['x', 'y', 'freq'])


def line_from_points(P: Point, Q: Point) -> Line:
    a = Q.y - P.y
    b = P.x - Q.x
    c = a*P.x + b*P.y

    return Line(a, b, c)


def calculate_antinodes(antenna_1: Antenna, antenna_2: Antenna) -> List[Point]:
    mag_1 = math.sqrt(math.pow(antenna_1.x, 2) + math.pow(antenna_1.y, 2))
    mag_2 = math.sqrt(math.pow(antenna_2.x, 2) + math.pow(antenna_2.y, 2))

    if mag_1 <= mag_2:
        min_antenna = antenna_1
        max_antenna = antenna_2
    else:
        min_antenna = antenna_2
        max_antenna = antenna_1

    d = Point(max_antenna.x - min_antenna.x, max_antenna.y - min_antenna.y)

    min_antinode = Point(min_antenna.x - d.x, min_antenna.y - d.y)
    max_antinode = Point(max_antenna.x + d.x, max_antenna.y + d.y)

    return [min_antinode, max_antinode]


def calculate_linear_antinodes(antenna_1: Antenna, antenna_2: Antenna, max_x, max_y) -> List[Point]:
    P = Point(antenna_1.x, antenna_1.y)
    Q = Point(antenna_2.x, antenna_2.y)

    line = line_from_points(P, Q)

    antinodes = list()

    for x in range(max_x):
        for y in range(max_y):
            if line.a*x + line.b*y == line.c:
                antinodes.append(Point(x, y))

    return antinodes


def print_map(grid: List[List[str]], antinodes: List[Point]) -> None:
    local_grid = deepcopy(grid)

    for antinode in antinodes:
        if local_grid[antinode.y][antinode.x] == '.':
            local_grid[antinode.y][antinode.x] = '#'

    rows = [''.join(row) + '\n' for row in local_grid]
    print(''.join(rows))


def main(map_file: str):
    with open(map_file, 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f.readlines()]

    antennas = [Antenna(x, y, freq) for y, row in enumerate(grid) for x, freq in enumerate(row) if freq != '.']

    antenna_dict = dict()

    for antenna in antennas:
        if antenna_dict.get(antenna.freq) is None:
            antenna_dict[antenna.freq] = [antenna]

        else:
            antenna_dict[antenna.freq].append(antenna)

    antinodes = list()

    for antenna_group in antenna_dict.values():
        for antenna_1, antenna_2 in itertools.combinations(antenna_group, 2):
            for antinode in calculate_antinodes(antenna_1, antenna_2):
                if antinode not in antinodes and antinode.x >= 0 and antinode.y >= 0 and antinode.x < len(grid[0]) and antinode.y < len(grid):
                    antinodes.append(antinode)

    print_map(grid, antinodes)
    print(f'Found {len(antinodes)} antinodes')

    antinodes = list()

    for antenna_group in antenna_dict.values():
        for antenna_1, antenna_2 in itertools.combinations(antenna_group, 2):
            for antinode in calculate_linear_antinodes(antenna_1, antenna_2, len(grid[0]), len(grid)):
                if antinode not in antinodes:
                    antinodes.append(antinode)

    print_map(grid, antinodes)
    print(f'Found {len(antinodes)} linear antinodes')


if __name__ == '__main__':
    main('map.txt')

