import numpy as np
import scipy.signal


def find_accessible_rolls(floor_matrix: np.ndarray) -> np.ndarray:
    convolution_matrix = np.ones((3, 3), dtype=np.int8)
    convolution_matrix[1][1] = 0

    surrounding_paper_rolls = scipy.signal.convolve2d(floor_matrix, convolution_matrix, mode='same')
    accessible_rolls = (surrounding_paper_rolls < 4) * floor_matrix

    return accessible_rolls


def remove_rolls(accessible_rolls: np.ndarray, floor_matrix: np.ndarray) -> np.ndarray:
    roll_mask = np.where((accessible_rolls == 0) | (accessible_rolls == 1), accessible_rolls ^ 1, accessible_rolls)

    return floor_matrix * roll_mask


def main():
    with open('floor_plan.txt', 'r') as f:
        floor_plan = [line.rstrip('\n') for line in f.readlines()]

    roll_matrix = np.zeros(shape=(len(floor_plan), len(floor_plan[0])), dtype=np.int8)

    for x, column in enumerate(floor_plan):
        for y, cell in enumerate(column):
            if cell == '@':
                roll_matrix[x][y] = 1

    print('Gnerated floor matrix')

    accessible_rolls = find_accessible_rolls(roll_matrix)
    number_of_accessible_rolls = np.sum(accessible_rolls)
    total_rolls_removed = number_of_accessible_rolls
    roll_matrix = remove_rolls(accessible_rolls, roll_matrix)

    print(f'There are {number_of_accessible_rolls} accessible rolls at the beginning')

    while number_of_accessible_rolls > 0:
        accessible_rolls = find_accessible_rolls(roll_matrix)
        number_of_accessible_rolls = np.sum(accessible_rolls)
        total_rolls_removed += number_of_accessible_rolls
        roll_matrix = remove_rolls(accessible_rolls, roll_matrix)

    print(f'A total of {total_rolls_removed} can be removed')


if __name__ == '__main__':
    main()
