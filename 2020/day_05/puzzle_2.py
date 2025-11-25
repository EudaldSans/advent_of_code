if __name__ == '__main__':
    with open('boarding_passes.tx') as f:
        ids = list()
        for line in f:  # read rest of lines
            directions = line.rstrip('\n')
            remaining_rows = 128
            remaining_columns = 8
            min_row = 0
            min_column = 0

            for pos in range(7):
                if line[pos] == 'B':
                    min_row += remaining_rows//2

                remaining_rows //= 2

            for pos in range(7, 10):
                if line[pos] == 'R':
                    min_column += remaining_columns//2

                remaining_columns //= 2

            ids.append(min_row*8 + min_column)

    possible_ids = range(max(ids))
    missing_ids = list()

    for ID in possible_ids:
        if ID not in ids and ID-1 in ids and ID +1 in ids:
            print(f'your ID is {ID}')
