from typing import List
import math


def get_fragments(value, fragment_size) -> List[int]:
    digits = 1 if value == 0 else math.floor(math.log10(value)) + 1
    number_of_fragments = digits // fragment_size

    most_significant_digits = 0

    fragment_list = list()

    for step in range(number_of_fragments, 0, -1):
        divider = 10 ** ((step - 1) * fragment_size)
        fragment = (value - most_significant_digits) // divider
        most_significant_digits += fragment * divider

        fragment_list.append(fragment)

    return fragment_list


def check_sequence(fragment_list: List[int]) -> bool:
    first = fragment_list.pop(0)

    for value in fragment_list:
        if value != first:
            return False

    return True


def find_invalid_ids_part_1(start: int, end: int) -> List[int]:
    invalid_ids = list()

    for value in range(start, end + 1):
        digits = 1 if value == 0 else math.floor(math.log10(value)) + 1

        if digits % 2 != 0:
            continue

        sequences = get_fragments(value, digits // 2)
        if len(sequences) == 0:
            continue

        if check_sequence(sequences):
            invalid_ids.append(value)

    return invalid_ids


def find_invalid_ids_part_2(start: int, end: int) -> List[int]:
    invalid_ids = list()

    for value in range(start, end + 1):
        digits = 1 if value == 0 else math.floor(math.log10(value)) + 1

        for fragment_size in range(1, digits // 2 + 1):
            if digits % fragment_size != 0:
                continue

            fragments = get_fragments(value, fragment_size)

            if check_sequence(fragments):
                invalid_ids.append(value)
                break

    return invalid_ids


def main():
    with open('id_ranges.txt', 'r') as f:
        line = f.readline().rstrip('\n')

    value_pairs = [pair for pair in line.split(',')]
    result_1 = 0
    result_2 = 0

    for pair in value_pairs:
        values = pair.split('-')

        start = int(values[0])
        end = int(values[1])

        for id in find_invalid_ids_part_1(start, end):
            result_1 += id

        for id in find_invalid_ids_part_2(start, end):
            result_2 += id

    print(f'The sum of all invalid ids for part 1: {result_1}')
    print(f'The sum of all invalid ids for part 2: {result_2}')


if __name__ == '__main__':
    main()
