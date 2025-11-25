from math import floor


if __name__ == '__main__':
    array =  list()

    with open('modules.tx') as file:
        total_fuel = 0
        for line in file:
            module_weight = int(line.strip())

            total_fuel += floor(module_weight/3) - 2

    print(f'Total fuel: {total_fuel}')
