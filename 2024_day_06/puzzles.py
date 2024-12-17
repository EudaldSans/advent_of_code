from collections import namedtuple
from typing import List
from copy import deepcopy

from tqdm import tqdm


Point = namedtuple('Point', ['x', 'y'])
Guard = namedtuple('Guard', ['x', 'y', 'dir'])


def find_guard(grid: List[List[str]]) -> Guard:
    for y, row in enumerate(grid):
        try:
            x = row.index('^')
            return Guard(x, y, 0)
        except ValueError:
            pass


def find_next_guard_position(x: int, y: int, direction: int) -> Point:
    match direction:
        case 0:
            return Point(x, y - 1)
        case 90:
            return Point(x + 1, y)
        case 180:
            return Point(x, y + 1)
        case 270:
            return Point(x - 1, y)
        case _:
            raise ValueError(f'Unknown guard direction {direction}')


def is_out_of_bounds(grid: List[List[str]], x: int, y: int) -> bool:
    return y >= len(grid) or x >= len(grid[0]) or y < 0 or x < 0


def move_guard(grid: List[List[str]], guard: Guard) -> Guard:
    current_dir = guard.dir
    next_position = find_next_guard_position(guard.x, guard.y, current_dir)

    if is_out_of_bounds(grid, next_position.x, next_position.y):
        return Guard(next_position.x, next_position.y, guard.dir)

    while grid[next_position.y][next_position.x] == '#':
        current_dir = (current_dir + 90) % 360
        next_position = find_next_guard_position(guard.x, guard.y, current_dir)

    return Guard(next_position.x, next_position.y, current_dir)


def add_obstacle_to_grid(grid: List[List[str]], obstacle: Point):
    new_grid = deepcopy(grid)
    new_grid[obstacle.y][obstacle.x] = '#'
    return new_grid


def print_map(grid: List[List[str]], guard: Guard) -> None:
    local_grid = deepcopy(grid)

    match guard.dir:
        case 0:
            guard_symbol = '^'
        case 90:
            guard_symbol = '>'
        case 180:
            guard_symbol = 'v'
        case 270:
            guard_symbol = '<'
        case _:
            raise ValueError(f'Unknown guard direction {guard.dir}')

    local_grid[guard.y][guard.x] = guard_symbol
    rows = [''.join(row) + '\n' for row in local_grid]
    print(''.join(rows))


def main(map_file):
    with open(map_file, 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f.readlines()]

    starting_guard = find_guard(grid)
    guard = starting_guard
    positions = list()

    grid[starting_guard.y][starting_guard.x] = '.'

    while not is_out_of_bounds(grid, guard.x, guard.y):
        current_pos = Point(guard.x, guard.y)

        if current_pos not in positions:
            positions.append(current_pos)

        guard = move_guard(grid, guard)

    print(f'Guard moved {len(positions)} times')

    loops = 0

    possible_grids = [add_obstacle_to_grid(grid, obstacle) for obstacle in tqdm(positions, desc='Adding obstacles')
                      if (obstacle.x != starting_guard.x or obstacle.y != starting_guard.y)]

    for new_grid in tqdm(possible_grids, desc='Checking grids'):
        guard = starting_guard
        past_guards = [starting_guard]
        while not is_out_of_bounds(new_grid, guard.x, guard.y):
            # print_map(new_grid, guard)
            guard = move_guard(new_grid, guard)

            if guard in past_guards:
                loops += 1
                break
            else:
                past_guards.append(guard)

    print(f'There are {loops} possible loops')


if __name__ == '__main__':
    main('map.txt')
