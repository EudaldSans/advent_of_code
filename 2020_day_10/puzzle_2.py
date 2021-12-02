import math


tribonacci = [0,1,1,2,4,7,13,24,44,81,149]


if __name__ == '__main__':
    with open('adapters.tx') as f:
        adapters = list()
        for line in f:  # read rest of lines
            adapters.append(int(line.rstrip('\n')))

    adapters.append(max(adapters) + 3)

    jolts = 0
    jumps_of_1 = 0
    combinations = 1

    while len(adapters) > 0:
        next_adapter = min(adapters)

        if next_adapter - jolts == 1:
            jumps_of_1 += 1
        elif next_adapter - jolts == 3:
            combinations *= tribonacci[jumps_of_1+1]
            jumps_of_1 = 0
        else:
            print('Something went wrong')

        jolts = next_adapter
        adapters.remove(next_adapter)

    print(f'There are {combinations} combinations possible')