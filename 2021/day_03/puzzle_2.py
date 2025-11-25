from typing import Tuple

import numpy as np


def find_most_common_bit(position: int, numbers: np.array) -> int:
    number_of_ones = 0
    length_of_numbers = len(numbers)

    for number in numbers:
        number_of_ones += number[position]

    # Return 1 if there is a tie as it satisfies tie conditions for scrubber and generator
    return int(number_of_ones >= length_of_numbers/2)


def split_by_most_common_bit(bit: int, position: int, numbers: np.array) -> Tuple[list, list]:
    array_by_most_common = list()
    array_by_least_common = list()

    for number in numbers:
        if number[position] == bit:
            array_by_most_common.append(number)
        else:
            array_by_least_common.append(number)

    return array_by_most_common, array_by_least_common


def main(diagnostic_path: str) -> None:
    with open(diagnostic_path) as diagnostic:
        numbers = diagnostic.read().split()
        numbers = np.array(list(map(list, numbers))).astype(int)

    most_common_bit = find_most_common_bit(0, numbers)
    generator_array, scrubber_array = split_by_most_common_bit(most_common_bit, 0, numbers)

    position = 1
    while len(generator_array) > 1:
        most_common_bit = find_most_common_bit(position, generator_array)

        generator_array, _ = split_by_most_common_bit(most_common_bit, position, generator_array)
        position += 1

    position = 1
    while len(scrubber_array) > 1:
        most_common_bit = find_most_common_bit(position, scrubber_array)

        _, scrubber_array = split_by_most_common_bit(most_common_bit, position, scrubber_array)
        position += 1

    scrubber_array = scrubber_array[0]
    generator_array = generator_array[0]

    generator_rate = 0
    for bit in generator_array:
        generator_rate = (generator_rate << 1) | bit

    scrubber_rate = 0
    for bit in scrubber_array:
        scrubber_rate = (scrubber_rate << 1) | bit

    print(f'Generator rate: ({generator_rate}, {generator_rate: 011b})')
    print(f'Scrubber rate: ({scrubber_rate}, {scrubber_rate: 011b})')
    print(f'Result is {generator_rate*scrubber_rate}')


if __name__ == '__main__':
    main('diagnostic_report.txt')
