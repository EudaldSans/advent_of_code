from typing import List, Dict


def get_distances_among_galaxies(universe: List[str], offset: int, row_status: Dict[int, bool], column_status: Dict[int, bool]) -> int:
    galaxies = list()
    y_offset = 0
    for y, row in enumerate(universe):
        x_offset = 0
        if not row_status[y]: y_offset += offset
        for x, char in enumerate(row):
            if not column_status[x]: x_offset += offset
            if char == '#':
                galaxies.append((y + y_offset, x + x_offset))

    distances = list()
    for count, galaxy in enumerate(galaxies):
        if count + 1 >= len(galaxies): break
        for paired_galaxy in galaxies[count + 1:]:
            distances.append(abs(paired_galaxy[0] - galaxy[0]) + abs(paired_galaxy[1] - galaxy[1]))

    return sum(distances)


def main(pipe_map_path: str) -> None:
    with open(pipe_map_path, 'r') as pipes_file:
        pipe_lines = pipes_file.readlines()
        universe = [line.strip('\n') for line in pipe_lines]

    column_status = dict()
    row_status = dict()

    for y in range(len(universe)):
        column_status[y] = False

    for x in range(len(universe)):
        row_status[x] = False

    for y, row in enumerate(universe):
        for x, char in enumerate(row):
            if char == '#':
                row_status[y] = True
                column_status[x] = True

    conservative_distances = get_distances_among_galaxies(universe, 1, row_status, column_status)
    expanded_distances = get_distances_among_galaxies(universe, 999999, row_status, column_status)

    print(f'The total sum of conservative distances is {conservative_distances}')
    print(f'The total sum of expanded distances is {expanded_distances}')


if __name__ == '__main__':
    main('galaxy_map.txt')