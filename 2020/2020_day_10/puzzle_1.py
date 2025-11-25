if __name__ == '__main__':
    with open('adapters.tx') as f:
        adapters = list()
        for line in f:  # read rest of lines
            adapters.append(int(line.rstrip('\n')))

    adapters.append(max(adapters) + 3)

    jolts = 0
    jumps_of_1 = 0
    jumps_of_3 = 0

    while len(adapters) > 0:
        next_adapter = min(adapters)

        if next_adapter - jolts == 1:
            jumps_of_1 += 1
        elif next_adapter - jolts == 3:
            jumps_of_3 += 1
        else:
            print('Something went wrong')

        jolts = next_adapter
        adapters.remove(next_adapter)

    print(f'There are {jumps_of_1} jumps of 1 Jolt and {jumps_of_3} jumps of 3 Jolts. Result is: {jumps_of_1*jumps_of_3}')