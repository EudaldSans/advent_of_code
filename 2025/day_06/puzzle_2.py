import math


def main():
    with open('homework.txt') as f:
        puzzle_input = [line.rstrip('\n') for line in f.readlines()]

    numbers = puzzle_input[:-1]
    current_operation = ''
    number_list = list()

    result = 0

    max_len = 0
    for number in numbers:
        if len(number) > max_len:
            max_len = len(number)

    for count, number in enumerate(numbers):
        if len(number) < max_len:
            padding = ' '*(max_len-len(number))
            numbers[count] = number + padding

    for index in range(max_len):
        if index < len(puzzle_input[-1]):
            character = puzzle_input[-1][index]
            if character != ' ':
                current_operation = character

        new_number = ''.join([number[index] for number in numbers if number[index] != ' '])
        # print(new_number)

        if new_number != '' or index == max_len - 1:
            number_list.append(int(new_number))

        if new_number == '' or index == max_len - 1:
            if current_operation == '+':
                result += sum(number_list)

            if current_operation == '*':
                result += math.prod(number_list)

            number_list.clear()

    print(result)


if __name__ == '__main__':
    main()
