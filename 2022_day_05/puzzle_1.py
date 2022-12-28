from typing import List
import re


class CrateMover9000:
    def __init__(self, stack_list: List[str]):
        stack_positions = stack_list[-1].rstrip().replace(' ', '')

        self.item_piles  = dict()
        stack_list = [items[1::4] for items in stack_list[:-1]]

        for position in stack_positions:
            index = int(position) - 1
            item_list = [items[index] for items in stack_list if len(items) > index and items[index] != ' ']
            self.item_piles[position] = item_list

        self.pattern = re.compile('move ([0-9]+) from ([0-9]+) to ([0-9]+)')

    def __str__(self):
        str_list = list()

        for key, items in self.item_piles.items():
            str_list.append(f'{key} - {items}')

        return '\n'.join(str_list)

    def move(self, movement: str):
        _, items, orig, dest, _ = self.pattern.split(movement)
        print(f'move {items} from {orig} to {dest}')
        print(self.item_piles)

        origin_pile = self.item_piles[orig]
        destination_pile = self.item_piles[dest]
        number_of_items = int(items)

        while number_of_items > 0:
            destination_pile.insert(0, origin_pile.pop(0))
            number_of_items -= 1

    def get_top_positions(self):
        return_list = list()

        for items in self.item_piles.values():
            return_list.append(items[0])

        return ''.join(return_list)


def clean_line(line: str):
    return_line = line.rstrip()
    return_line = return_line.replace(' ', '')
    return_line = return_line.replace('[', '')
    return_line = return_line.replace(']', '')

    return return_line


def main(crane):
    with open('item_piles.txt') as items_file:
        stack_and_moves = items_file.readlines()

    stack_list = list()
    moves = list()
    for count, line in enumerate(stack_and_moves):
        if line == '\n':
            stack_list = stack_and_moves[:count]

            print(stack_list)
            moves = stack_and_moves[count + 1:]

    crane = crane(stack_list)
    print(crane)

    for move in moves:
        crane.move(move.rstrip())
        print(crane)

    print(f'The items at the top of the piles are: {crane.get_top_positions()}')


if __name__ == '__main__':
    main(CrateMover9000)