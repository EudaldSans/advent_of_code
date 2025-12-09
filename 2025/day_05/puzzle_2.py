

def main():
    with open('inventory_file.txt') as f:
        puzzle_input = f.read()

    fresh_ingredients = [tuple(map(int, line.rstrip('\n').split('-'))) for line in puzzle_input.splitlines()]

    print(fresh_ingredients)
    fresh_ingredients.sort()
    print(fresh_ingredients)

    merged_list = []
    low, high = fresh_ingredients[0]
    for new_low, new_high in fresh_ingredients[1:]:
        if new_low <= high + 1:
            high = max(high, new_high)
        else:
            merged_list.append((low, high))
            low, high = new_low, new_high
    merged_list.append((low, high))

    all_fresh = sum(hi - lo + 1 for lo, hi in merged_list)
    print(all_fresh)


if __name__ == '__main__':
    main()
