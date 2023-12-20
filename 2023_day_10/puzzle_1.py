from typing import Tuple, List
from collections import namedtuple

Point = Tuple[int, int]


pipe_moves = {'|': [(-1, 0), (1, 0)],
              '-': [(0, -1), (0, 1)],
              'L': [(-1, 0), (0, 1)],
              'J': [(0, -1), (-1, 0)],
              '7': [(0, -1), (1, 0)],
              'F': [(1, 0), (0, 1)]}


def find_start_position(grid: List[List[str]]) -> Point:
    return [(y, x) for y, row in enumerate(grid) for x, char in enumerate(row) if char == 'S'][0]


def find_valid_moves(grid: List[List[str]], current_position: Point, previous_position: Point = None) -> List[str]:
    possible_directions = pipe_moves[grid[current_position.y][current_position.x]]
    for dir in possible_directions:
        test_position = Point(current_position.x + dir.x, current_position.y + dir.y)


def find_starting_character(grid: List[List[str]], start_position: Point) -> Point:
    possible_directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    valid_directions = list()
    for direction in possible_directions:
        test_position = (direction[0] + start_position[0], direction[1] + start_position[1])
        test_character = grid[test_position[0]][test_position[1]]

        if test_character not in pipe_moves.keys():
            continue

        test_directions = pipe_moves[test_character]
        print(f'{test_character=} with {test_directions=} for {direction=}')
        if direction == (1, 0) and (-1, 0) in test_directions: valid_directions.append(direction)
        if direction == (-1, 0) and (1, 0) in test_directions: valid_directions.append(direction)
        if direction == (0, 1) and (0, -1) in test_directions: valid_directions.append(direction)
        if direction == (0, -1) and (0, 1) in test_directions: valid_directions.append(direction)

    for pipe, directions in pipe_moves.items():
        if directions == valid_directions:
            return pipe

    raise ValueError(f'Invalid directions: {valid_directions}')


'''def determine_starting_char(grid: List[List[str]]) -> str:
    valid_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    next_positions = []

    for pipe, move in pipe_map.items():'''


def main():
    grid = [['.', '.', '.', '.', '.'],
            ['.', 'S', '-', '7', '.'],
            ['.', '|', '.', '|', '.'],
            ['.', 'L', '-', 'J', '.'],
            ['.', '.', '.', '.', '.']]

    start_pos = find_start_position(grid)
    print(find_starting_character(grid, start_pos))


if __name__ == '__main__':
    main()
