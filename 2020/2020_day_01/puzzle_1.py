if __name__ == '__main__':
    array = list()
    with open('numbers.txt') as f:
        for line in f:  # read rest of lines
            array.append(int(line))

    print(array)

    correct_numbers = list()
    while len(correct_numbers) == 0:
        for count in range(len(array)):
            if array[0]+array[count] == 2020:
                print('found numbers')
                correct_numbers = [array[0], array[count]]
                print(correct_numbers)

                break

        array.pop(0)

    print(f'result is: {correct_numbers[0]*correct_numbers[1]}')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
