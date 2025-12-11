from itertools import combinations
from typing import Tuple, List
from tqdm import tqdm


def area(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def count_intersects(edges: List[Tuple[Tuple[int, int]]], square: Tuple[Tuple[int, int]]) -> int:
    count = 0

    tile_left = min(square[0][0], square[1][0])
    tile_right = max(square[0][0], square[1][0])

    tile_top = min(square[0][1], square[1][1])
    tile_bottom = max(square[0][1], square[1][1])

    for edge_a, edge_b in edges:
        edge_left = min(edge_a[0], edge_b[0])
        edge_right = max(edge_a[0], edge_b[0])

        edge_top = min([edge_a[1], edge_b[1]])
        edge_bottom = max([edge_a[1], edge_b[1]])

        is_left = edge_left > tile_right
        is_right = edge_right < tile_left
        is_up = edge_top > tile_bottom
        is_down = edge_bottom < tile_top

        if not (is_left or is_right or is_up or is_down):
            count += 1

    return count


def square_intersects(edges: List[Tuple[Tuple[int, int]]], square: Tuple[Tuple[int, int]]) -> bool:
    tile_left = min(square[0][0], square[1][0])
    tile_right = max(square[0][0], square[1][0])

    tile_top = min(square[0][1], square[1][1])
    tile_bottom = max(square[0][1], square[1][1])

    for edge_a, edge_b in edges:
        edge_left = min(edge_a[0], edge_b[0])
        edge_right = max(edge_a[0], edge_b[0])

        edge_top = min([edge_a[1], edge_b[1]])
        edge_bottom = max([edge_a[1], edge_b[1]])

        is_left = edge_left >= tile_right
        is_right = edge_right <= tile_left
        is_up = edge_top >= tile_bottom
        is_down = edge_bottom <= tile_top

        if not (is_left or is_right or is_up or is_down):
            return True

    return False


def main():
    with open('tile_grid.txt', 'r') as f:
        red_tiles = [tuple(map(int, l.rstrip('\n').split(','))) for l in f.readlines()]

    ordered_squares = sorted(combinations(red_tiles, 2), key=lambda pq: area(*pq))

    print(f'The largest possible area is: {area(*ordered_squares[-1])}')

    edges = list()
    for count, tile in enumerate(red_tiles[:-1]):
        edges.append((tile, red_tiles[count + 1]))

    edges.append((red_tiles[0], red_tiles[-1]))

    possible_squares = list()
    for square in tqdm(ordered_squares, desc='Removing intersecting squares'):
        if not square_intersects(edges, square):
            possible_squares.append(square)

    squares_inside_shape = list()
    for square in tqdm(possible_squares, desc='Finding squares inside the shape'):
        x = min(square[0][0], square[1][0])
        y = min(square[0][1], square[1][1])

        line = ((x, y), (x, 0))
        possible_edges = [edge for edge in edges if (edge[0][0] <= x or edge[1][0] <= x) and edge[0][0] != edge[1][0]]
        crossings = count_intersects(possible_edges, line)

        if crossings % 2 != 0:
            squares_inside_shape.append(square)

    print(f'The largest possible area with only red and green tiles is: {area(*squares_inside_shape[-1])}')


if __name__ == '__main__':
    main()
