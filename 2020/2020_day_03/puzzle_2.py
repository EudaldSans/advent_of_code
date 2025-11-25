if __name__ == '__main__':
    array = list()
    with open('map.tx') as f:
        for line in f:  # read rest of lines
            array.append(line.rsplit()[0])

    results = list()
    slopes_to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    length = len(array)

    for slope in slopes_to_check:
        step_x, step_y = slope
        pos_x = 0
        trees_found = 0

        for pos_y in range(0, length, step_y):
            line = array[pos_y]
            if line[pos_x] == '#':
                trees_found += 1

            pos_x += step_x
            pos_x = pos_x % len(line)

        results.append(trees_found)
        print(f'Found {trees_found} trees')

    print(results)
    final_result = 1
    for result in results:
        final_result *= result

    print(f'Final result is {final_result}')