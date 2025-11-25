import re

instruction_re = re.compile('([A-Z])([0-9]+)')
waypoint = [1, 10, 0, 0]  # N,E,S,W

if __name__ == '__main__':
    with open('instructions.tx') as f:
        ferry_pos = [0, 0, 0, 0]  # N,E,S,W

        for line in f:  # read rest of lines
            _, direction, units, _ = instruction_re.split(line.rstrip('\n'))

            if direction == 'N':
                waypoint[0] += int(units)
            if direction == 'E':
                waypoint[1] += int(units)
            if direction == 'S':
                waypoint[2] += int(units)
            if direction == 'W':
                waypoint[3] += int(units)
            if direction == 'F':
                ferry_pos = [x + int(units)*y for x, y in zip(ferry_pos, waypoint)]
            if direction == 'L':
                count = int(units) / 90
                while count > 0:
                    waypoint = waypoint[1:] + waypoint[:1]
                    count -= 1
            if direction == 'R':
                count = int(units) / 90
                while count > 0:
                    waypoint = waypoint[3:] + waypoint[:3]
                    count -= 1

    north_south = ferry_pos[0] - ferry_pos[2]
    east_west = ferry_pos[1] - ferry_pos[3]

    print(f'Ferry moved {north_south}N, and {east_west}E. Total {abs(north_south) + abs(east_west)}')
