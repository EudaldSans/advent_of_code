from typing import Tuple


def rotation(distance: int, pointer: int, direction: str) -> Tuple[int, int]:
    crossings = 0

    for _ in range(distance):
        if direction == 'L':
            pointer -= 1
        elif direction == 'R':
            pointer += 1

        pointer = pointer % 100

        if pointer == 0:
            crossings += 1

    return crossings, pointer


def main():
    with open('safe_combination.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    values = [(line[0], int(line[1:])) for line in lines]

    pointer = 50
    number_of_crosses = 0

    for direction, distance in values:
        crossings, pointer = rotation(distance, pointer, direction)

        print(pointer)

        number_of_crosses += crossings

    print(f'The door combination is: {number_of_crosses}')


if __name__ == '__main__':
    main()
