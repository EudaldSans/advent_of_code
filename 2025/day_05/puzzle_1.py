import utils.ranges as ranges


def main():
    fresh_ids = list()
    ingredients = list()

    with open('inventory_file.txt', 'r') as f:
        lines = f.readlines()

    for count, line in enumerate(lines):
        if line == '\n':
            ingredients = lines[count + 1:]
            break

        fresh_ids.append(line)

    fresh_ids = [id.rstrip('\n').split('-') for id in fresh_ids]
    fresh_ranges = [ranges.Range(int(id[0]), int(id[1])) for id in fresh_ids]
    checker = ranges.InclusiveRangeChecker(fresh_ranges)

    ingredients = [int(id.rstrip('\n')) for id in ingredients]
    fresh_ingredients = 0

    for ingredient in ingredients:
        if ingredient in checker:
            fresh_ingredients += 1
            continue

    print(f'There are {fresh_ingredients} fresh ingredients')


if __name__ == '__main__':
    main()
