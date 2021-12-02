from math import floor


if __name__ == '__main__':
    array = list()

    with open('modules.tx') as file:
        total_fuel = 0
        for line in file:
            module_weight = int(line.strip())
            fuel_for_module = floor(module_weight/3) - 2
            total_fuel += fuel_for_module

            new_fuel = floor(fuel_for_module/3) - 2

            while new_fuel > 0:
                total_fuel += new_fuel
                new_fuel = floor(new_fuel / 3) - 2

    print(f'Total fuel: {total_fuel}')
