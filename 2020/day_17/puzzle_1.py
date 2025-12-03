import numpy as np


class Matrix:
    INACTIVE_CUBE = 0
    ACTIVE_CUBE = 1

    def __init__(self, initial_size: int, number_of_cycles):

        max_size = initial_size + number_of_cycles * 2
        self.matrix = np.zeros(shape=[number_of_cycles + 2 + 1, max_size, max_size], dtype=np.int8)

    def activate_cube(self, x: int, y: int, z: int):
        self.matrix[z][x][y] = Matrix.ACTIVE_CUBE

    def __repr__(self):
        return str(self.matrix)


def main():
    with open('example.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    initial_size = len(lines)
    number_of_cycles = 2

    initial_z = initial_size // 2 + number_of_cycles
    xy_offset = number_of_cycles

    matrix = Matrix(initial_size, number_of_cycles)

    for x, row in enumerate(lines):
        for y, cell in enumerate(row):
            if cell == '#':
                matrix.activate_cube(x + xy_offset, y + xy_offset, initial_z)


    print(matrix)




if __name__ == '__main__':
    main()
