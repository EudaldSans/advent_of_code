if __name__ == '__main__':
    with open('transmission.tx') as f:
        transmission = list()
        for line in f:  # read rest of lines
            transmission.append(int(line.rstrip('\n')))

    preamble = list()
    for new_num in transmission:
        line_is_exploit = True

        if len(preamble) < 25:
            preamble.append(new_num)
            continue

        for num in preamble:
            if (new_num - num) in preamble and (new_num - num) != num:
                line_is_exploit = False
                break

        if line_is_exploit:
            exploit = new_num
            break

        preamble.pop(0)
        preamble.append(new_num)

    print(f'Exploit is number {exploit}')  # 248131121

    finished_checking = False

    for count, num in enumerate(transmission):
        total = 0
        index = count
        finished_checking = False
        while not finished_checking:
            total += transmission[index]

            if total >= exploit:
                finished_checking = True

            index += 1

        if total == exploit:
            result = min(transmission[count:index]) + max(transmission[count:index])
            break

    print(transmission[count:index])
    print(f'Sum of contiguous numbers is {result}')
