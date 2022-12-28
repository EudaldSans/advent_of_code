from puzzle_1 import CrateMover9000, main

class CrateMover9001(CrateMover9000):
    def move(self, movement: str):
        _, items, orig, dest, _ = self.pattern.split(movement)

        origin_pile = self.item_piles[orig]
        destination_pile = self.item_piles[dest]
        number_of_items = int(items)

        while number_of_items > 0:
            destination_pile.insert(0, origin_pile.pop(number_of_items - 1))
            number_of_items -= 1


if __name__ == '__main__':
    main(CrateMover9001)
