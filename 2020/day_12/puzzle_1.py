import re

instruction_re = re.compile('([A-Z])([0-9]+)')
facings = [1, 2, 3, 0]  # E,S,W,N

if __name__ == '__main__':
    with open('instructions.tx') as f:
        ferry_pos = [0, 0, 0, 0]  # N,E,S,W

        for line in f:  # read rest of lines
            _, direction, units, _ = instruction_re.split(line.rstrip('\n'))

            if direction == 'N':
                ferry_pos[0] += int(units)
            if direction == 'E':
                ferry_pos[1] += int(units)
            if direction == 'S':
                ferry_pos[2] += int(units)
            if direction == 'W':
                ferry_pos[3] += int(units)
            if direction == 'F':
                ferry_pos[facings[0]] += int(units)
            if direction == 'R':
                count = int(units)/90
                while count > 0:
                    facings = facings[1:] + facings[:1]
                    count -= 1
            if direction == 'L':
                count = int(units)/90
                while count > 0:
                    facings = facings[3:] + facings[:3]
                    count -= 1

    north_south = ferry_pos[0] - ferry_pos[2]
    east_west = ferry_pos[1] - ferry_pos[3]

    print(ferry_pos)
    print(f'Ferry moved {north_south}N, and {east_west}E. Total {abs(north_south) + abs(east_west)}')
