

def main():
    with open('homework.txt') as f:
        puzzle_input = [line.rstrip('\n') for line in f.readlines()]

    operators = [line.rstrip('\n').split(' ')[0] for line in puzzle_input[-1]]
    operators = [operator for operator in operators if operator != '']

    numbers_list = [line.rstrip('\n').split(' ') for line in puzzle_input[:-1]]
    numbers_list = [[int(number) for number in line if number != ''] for line in numbers_list]

    total = 0

    for index, operator in enumerate(operators):
        if operator == '+':
            result = 0
            for numbers in numbers_list:
                result += numbers[index]

        if operator == '*':
            result = 1
            for numbers in numbers_list:
                result *= numbers[index]

        total += result

    print(total)


if __name__ == '__main__':
    main()
