

def main():
    with open('safe_combination.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    values = [(line[0], int(line[1:])) for line in lines]

    pointer = 50
    number_of_crosses = 0

    for direction, distance in values:
        if direction == 'L':
            pointer -= distance
        elif direction == 'R':
            pointer += distance
        else:
            raise ValueError(f'Unknown turn direction {direction}')

        pointer = pointer % 100

        if pointer == 0:
            number_of_crosses += 1

        if pointer > 100 or pointer < 0:
            raise ValueError(f'Pointer is not within limits {pointer}')

    print(f'The door combination is: {number_of_crosses}')


if __name__ == '__main__':
    main()
