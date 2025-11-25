import re


def find_occupied_neighboring_seats(x, y, _layout):
    _line = _layout[y]
    occupied_seats = 0

    # N
    new_y = y - 1
    while new_y >= 0:
        if _layout[new_y][x] == '.':
            new_y -= 1
            continue
        elif _layout[new_y][x] == '#':
            occupied_seats += 1
            break
        else:
            break

    # NE
    new_x = x + 1
    new_y = y - 1
    while new_x < len(line) and new_y >= 0:
        if _layout[new_y][new_x] == '.':
            new_x += 1
            new_y -= 1
            continue
        elif _layout[new_y][new_x] == '#':
            occupied_seats += 1
            break
        else:
            break

    # E
    new_x = x + 1
    while new_x < len(line):
        if _layout[y][new_x] == '.':
            new_x += 1
            continue
        elif _layout[y][new_x] == '#':
            occupied_seats += 1
            break
        else:
            break

    # SE
    new_x = x + 1
    new_y = y + 1
    while new_x < len(line) and new_y < len(_layout):
        if _layout[new_y][new_x] == '.':
            new_x += 1
            new_y += 1
            continue
        elif _layout[new_y][new_x] == '#':
            occupied_seats += 1
            break
        else:
            break

    # S
    new_y = y + 1
    while new_y < len(_layout):
        if _layout[new_y][x] == '.':
            new_y += 1
            continue
        elif _layout[new_y][x] == '#':
            occupied_seats += 1
            break
        else:
            break

    # SW
    new_x = x - 1
    new_y = y + 1
    while new_x >= 0 and new_y < len(_layout):
        if _layout[new_y][new_x] == '.':
            new_x -= 1
            new_y += 1
            continue
        elif _layout[new_y][new_x] == '#':
            occupied_seats += 1
            break
        else:
            break

    # W
    new_x = x - 1
    while new_x >= 0:
        if _layout[y][new_x] == '.':
            new_x -= 1
            continue
        elif _layout[y][new_x] == '#':
            occupied_seats += 1
            break
        else:
            break

    # NW
    new_x = x - 1
    new_y = y - 1
    while new_x >= 0 and new_y >= 0:
        if _layout[new_y][new_x] == '.':
            new_x -= 1
            new_y -= 1
            continue
        elif _layout[new_y][new_x] == '#':
            occupied_seats += 1
            break
        else:
            break

    return occupied_seats


if __name__ == '__main__':
    with open('seat_layout.tx') as f:
        total_questions = 0
        layout = list()
        for line in f:  # read rest of lines
            layout.append(line.rstrip('\n'))

    new_layout = layout
    print('\n'.join(k for k in new_layout))
    print('\n')
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
                    if find_occupied_neighboring_seats(x, y, layout) == 0:
                        new_line += '#'
                    else:
                        new_line += 'L'

                elif seat == '#':
                    if find_occupied_neighboring_seats(x, y, layout) > 4:
                        new_line += 'L'
                    else:
                        new_line += '#'

                else:
                    print('something went wrong')

            new_layout.append(new_line)

        print('\n'.join(k for k in new_layout))
        print('\n')

    occupied_seats = 0

    for line in new_layout:
        occupied_seats += len(re.findall('#', line))

    print(f'In the end there are {occupied_seats} occupied seats. ')

