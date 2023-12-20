from typing import Tuple, List, Optional
from collections import namedtuple

Point = Tuple[int, int]


pipe_moves = {'|': [(-1, 0), (1, 0)],
              '-': [(0, -1), (0, 1)],
              'L': [(0, 1), (-1, 0)],
              'J': [(0, -1), (-1, 0)],
              '7': [(1, 0), (0, -1)],
              'F': [(1, 0), (0, 1)],
              'S': [(1, 0), (0, 1), (0, -1), (-1, 0)]}


def find_start_position(grid: List[List[str]]) -> Point:
    return [(y, x) for y, row in enumerate(grid) for x, char in enumerate(row) if char == 'S'][0]


def find_starting_character(grid: List[List[str]], start_position: Point) -> Point:
    valid_directions = find_valid_directions(grid, start_position, None)
    for pipe, directions in pipe_moves.items():
        if directions == valid_directions:
            return pipe

    raise ValueError(f'Invalid directions: {valid_directions}')


def find_valid_directions(grid: List[List[str]], current_pos: Point, prev_dir: Optional[Point]) -> List[Point]:
    current_pipe = grid[current_pos[0]][current_pos[1]]
    possible_directions = pipe_moves[current_pipe]
    valid_dirs = list()
    for direction in possible_directions:
        test_pos = (direction[0] + current_pos[0], direction[1] + current_pos[1])
        if test_pos[0] < 0 or test_pos[0] >= len(grid): continue
        if test_pos[1] < 0 or test_pos[1] >= len(grid[0]): continue

        test_char = grid[test_pos[0]][test_pos[1]]

        if test_char not in pipe_moves.keys():
            continue

        test_dirs = pipe_moves[test_char]
        if direction == (1, 0) and (-1, 0) in test_dirs and prev_dir != (-1, 0):
            valid_dirs.append(direction)
        if direction == (-1, 0) and (1, 0) in test_dirs and prev_dir != (1, 0):
            valid_dirs.append(direction)
        if direction == (0, 1) and (0, -1) in test_dirs and prev_dir != (0, -1):
            valid_dirs.append(direction)
        if direction == (0, -1) and (0, 1) in test_dirs and prev_dir != (0, 1):
            valid_dirs.append(direction)

    return valid_dirs


def main(pipe_map_path: str) -> int:
    with open(pipe_map_path, 'r') as pipes_file:
        pipe_lines = pipes_file.readlines()
        clean_lines = [line.strip('\n') for line in pipe_lines]

    grid = [[char for char in row] for row in clean_lines]

    start_pos = find_start_position(grid)
    start_dir = find_valid_directions(grid, start_pos, None)[0]
    start_char = find_starting_character(grid, start_pos)

    grid[start_pos[0]][start_pos[1]] = start_char

    prev_dir = start_dir
    current_pos = (start_pos[0] + start_dir[0], start_pos[1] + start_dir[1])

    loop = [start_pos, current_pos]
    while current_pos != start_pos:
        loop.append(current_pos)
        current_dir = find_valid_directions(grid, current_pos, prev_dir)[0]
        current_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])

        prev_dir = current_dir

    print(f'Loop has {len(loop)} pipes, should find the animal at pipe number {len(loop)//2}')

    tiles_within_loop = list()
    for y in range(len(grid)):
        inside_loop = False
        for x in range(len(grid[0])):
            pos = (y, x)

            if pos in loop and grid[y][x] in ['|', 'J', 'L']: inside_loop = not inside_loop
            if pos not in loop and inside_loop: tiles_within_loop.append(pos)

    for pos in tiles_within_loop:
        grid[pos[0]][pos[1]] = 'I'

    for row in grid:
        print(''.join(row))

    print(f'There are {len(tiles_within_loop)} tiles inside of the loop')



if __name__ == '__main__':
    main('pipe_map.txt')
