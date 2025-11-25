if __name__ == '__main__':
    with open('transmission.tx') as f:
        total_questions = 0
        preamble = list()
        for line in f:  # read rest of lines
            line_is_exploit = True
            new_num = int(line.rstrip('\n'))

            if len(preamble) < 25:
                preamble.append(new_num)
                continue

            for num in preamble:
                if (new_num - num) in preamble and (new_num - num) != num:
                    line_is_exploit = False
                    break

            if line_is_exploit:
                break

            preamble.pop(0)
            preamble.append(new_num)

    print(f'Exploit is number {line}')

