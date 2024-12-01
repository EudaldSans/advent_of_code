import numpy as np


def puzzle_1(list_1: np.ndarray, list_2: np.ndarray):
    list_1.sort()
    list_2.sort()

    print(f'The distance between lists is:{sum(abs(list_1 - list_2))}')


def puzzle_2(list_1: np.ndarray, list_2: np.ndarray):
    similarity_score = 0

    for item in list_1:
        similarity_score += item * np.count_nonzero(list_2 == item)

    print(f'The similarity score is {similarity_score}')


def main(file_name: str) -> None:
    list_1 = list()
    list_2 = list()

    with open(file_name, 'r') as file:
        location_ids = file.readlines()

    location_ids = [line.strip('\n').split('   ') for line in location_ids]
    list_1 = np.array([int(location_id[0]) for location_id in location_ids])
    list_2 = np.array([int(location_id[1]) for location_id in location_ids])

    puzzle_1(list_1, list_2)
    puzzle_2(list_1, list_2)


if __name__ == '__main__':
    main('location_ids.txt')
