if __name__ == '__main__':
    array = list()
    with open('map.tx') as f:
        for line in f:  # read rest of lines
            array.append(line.rsplit()[0])

    pos_x = 0
    trees_found = 0

    for pos_y, line in enumerate(array):
        if line[pos_x] == '#':
            trees_found += 1

        pos_x += 3
        pos_x = pos_x % len(line)

    print(f'Found {trees_found} trees')
