import numpy as np
import scipy.signal
import sys


class Matrix:
    INACTIVE_CUBE = 0
    ACTIVE_CUBE = 1

    def __init__(self, initial_size: int, number_of_cycles: int, dimensions: int):

        max_size = initial_size + number_of_cycles * 2
        shape = (max_size,) * dimensions

        self.matrix = np.zeros(shape=shape, dtype=np.int8)
        self.dimensions = dimensions

    def __repr__(self):
        return str(self.matrix)

    def activate_cube(self, x: int, y: int):
        offset = self.matrix.shape[0] // 2 + 1
        index = [offset] * self.dimensions

        index[-2] = x
        index[-1] = y

        index = tuple(index)
        self.matrix[index] = Matrix.ACTIVE_CUBE

    def perform_cycle(self):
        shape = (3,) * self.dimensions
        convolution_matrix = np.ones(shape, dtype=np.int8)
        center_index = (1,) * self.dimensions

        convolution_matrix[center_index] = 0

        number_of_neighbors = scipy.signal.convolve(self.matrix, convolution_matrix, mode='same')

        active_cells_neighbors = number_of_neighbors * self.matrix
        cells_to_deactivate = np.logical_and(active_cells_neighbors != 2, active_cells_neighbors != 3)

        inactive_cells_neighbors = number_of_neighbors * (np.logical_not(self.matrix))
        cells_to_activate = inactive_cells_neighbors == 3

        self.matrix = self.matrix * np.logical_not(cells_to_deactivate) + cells_to_activate

    def evaluate_matrix(self) -> int:
        return np.sum(self.matrix)


def main():
    np.set_printoptions(threshold=sys.maxsize)

    with open('initial_configuration.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    initial_size = len(lines)
    number_of_cycles = 6

    offset = number_of_cycles

    cube = Matrix(initial_size, number_of_cycles, 3)
    hyper_cube = Matrix(initial_size, number_of_cycles, 4)

    for x, row in enumerate(lines):
        for y, cell in enumerate(row):
            if cell == '#':
                cube.activate_cube(x + offset, y + offset)
                hyper_cube.activate_cube(x + offset, y + offset)

    for cycle in range(number_of_cycles):
        cube.perform_cycle()
        hyper_cube.perform_cycle()

    print(f'After {number_of_cycles} cycles, there are {cube.evaluate_matrix()} active cubes')
    print(f'After {number_of_cycles} cycles, there are {hyper_cube.evaluate_matrix()} active hyper cubes')


if __name__ == '__main__':
    main()
