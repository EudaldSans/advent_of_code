import re


def find_neighboring_seats(x, y, layout):
    _line = layout[y]

    if x == 0:
        x_min = x
        x_max = x + 1
    elif x >= len(_line) - 1:
        x_min = x - 1
        x_max = x
    else:
        x_min = x - 1
        x_max = x + 1

    if y == 0:
        string = layout[y][x_min:x_max+1] + layout[y + 1][x_min:x_max+1]
    elif y == len(layout) - 1:
        string = layout[y - 1][x_min:x_max+1] + layout[y][x_min:x_max+1]
    else:
        string = layout[y - 1][x_min:x_max+1] + layout[y][x_min:x_max+1] + layout[y + 1][x_min:x_max+1]

    return string


if __name__ == '__main__':
    with open('seat_layout.tx') as f:
        total_questions = 0
        layout = list()
        for line in f:  # read rest of lines
            layout.append(line.rstrip('\n'))

    new_layout = layout
    first_run = True

    while layout != new_layout or first_run:
        first_run = False
        layout = new_layout
        new_layout = list()

        for y, line in enumerate(layout):
            new_line = ''
            for x, seat in enumerate(line):
                if seat == '.':
                    new_line += '.'

                elif seat == 'L':
                    string = find_neighboring_seats(x, y, layout)
                    if len(re.findall('#', string)) == 0:
                        new_line += '#'
                    else:
                        new_line += 'L'

                elif seat == '#':
                    string = find_neighboring_seats(x, y, layout)
                    if len(re.findall('#', string)) > 4:
                        new_line += 'L'
                    else:
                        new_line += '#'

                else:
                    print('something went wrong')

            new_layout.append(new_line)

    occupied_seats = 0

    for line in new_layout:
        occupied_seats += len(re.findall('#', line))

    print(f'In the end there are {occupied_seats} occupied seats. ')

