from typing import List


class Elf:
    def __init__(self, calorie_list: List[int]):
        self.calorie_list = calorie_list

    def get_total_calories(self) -> int:
        return sum(self.calorie_list)


def main():
    with open('calories_list.txt') as items_file:
        item_list = items_file.readlines()

    item_list = [item.rstrip('\n') for item in item_list]
    item_list.append('')

    elf_items = list()
    calories_list = list()

    for item in item_list:
        if not item:
            calories_list.append(sum(elf_items))
            elf_items.clear()
            continue

        elf_items.append(int(item))

    print(f'The first elf with the highest ammount of calories has {max(calories_list)} calories')
    top_three_elves = max(calories_list)
    calories_list.remove(max((calories_list)))

    print(f'The second elf with the highest ammount of calories has {max(calories_list)} calories')
    top_three_elves += max(calories_list)
    calories_list.remove(max((calories_list)))

    print(f'The third elf with the highest ammount of calories has {max(calories_list)} calories')
    top_three_elves += max(calories_list)

    print(f'The top three elves have {top_three_elves} calories together')


if __name__ == '__main__':
    main()

