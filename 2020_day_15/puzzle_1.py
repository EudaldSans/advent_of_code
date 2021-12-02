

def main(file_path, last_turn):
    with open(file_path) as starting_numbers:
        numbers = starting_numbers.readline().split(',')
        numbers = list(map(int, numbers))

    number_turn = dict()

    last_number_spoken = numbers.pop(0)
    turn = 1
    for turn, new_number_spoken in enumerate(numbers, start=turn):
        number_turn.setdefault(last_number_spoken, turn - 1)
        last_number_spoken = new_number_spoken

    for turn in range(turn, last_turn - 1):
        turn_when_number_was_spoken = number_turn.get(last_number_spoken, turn)
        number_turn[last_number_spoken] = turn
        last_number_spoken = turn - turn_when_number_was_spoken

    print(f'{last_turn}th spoken is {last_number_spoken}')


if __name__ == '__main__':
    main('example_0.txt', 2020)
    main('example_1.txt', 2020)
    main('example_2.txt', 2020)
    main('example_3.txt', 2020)
    main('example_4.txt', 2020)
    main('example_5.txt', 2020)
    main('example_6.txt', 2020)
    main('input.txt', 2020)

    main('example_0.txt', 30000000)
    main('example_1.txt', 30000000)
    main('example_2.txt', 30000000)
    main('example_3.txt', 30000000)
    main('example_4.txt', 30000000)
    main('example_5.txt', 30000000)
    main('example_6.txt', 30000000)
    main('input.txt', 30000000)
