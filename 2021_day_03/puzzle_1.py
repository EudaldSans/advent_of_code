import numpy as np


def find_most_common_bits(number_list: np.array) -> list:
    length_of_list = len(number_list)
    most_common_bits = list()

    accumulated_ones = np.sum(number_list, axis=0)

    for bit in accumulated_ones:
        most_common_bits.append(int(bit > length_of_list/2))

    return most_common_bits


def main(diagnostic_path):
    with open(diagnostic_path) as diagnostic:
        numbers = diagnostic.read().split()
        numbers = np.array(list(map(list, numbers))).astype(int)

    most_common_bits = find_most_common_bits(numbers)

    gamma_rate = 0
    epsilon_rate = 0
    for bit in most_common_bits:
        gamma_rate = (gamma_rate << 1) | bit
        epsilon_rate = (epsilon_rate << 1) | (not bit)

    print(f'Result is: {gamma_rate*epsilon_rate}')


if __name__ == '__main__':
    main('diagnostic_report.txt')
