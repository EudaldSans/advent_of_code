from typing import List


class X_MASFinder:
    def __init__(self, word_search: List[str]):
        self.word_search = word_search
        self.word_to_search = 'MAS'
        self.word_len = len('MAS')

        self.x_size = len(word_search[0])
        self.y_size = len(word_search)

    def check_pos(self, x: int, y: int) -> bool:
        if x >= self.x_size or y >= self.y_size:
            raise ValueError()

        if self.word_search[y][x] != 'A':
            return False

        if y == 0 or x == 0 or y == self.y_size - 1 or x == self.x_size  - 1:
            return False

        str_1 = ''.join(self.word_search[y + a][x + a] for a in range(-1, 2))
        str_2 = ''.join(self.word_search[y - a][x + a] for a in range(-1, 2))

        if (str_1 == 'MAS' or str_1 == 'SAM') and (str_2 == 'MAS' or str_2 == 'SAM'):
            return True

        return False


def puzzle_2(word_search_file: str):
    with open(word_search_file, 'r') as f:
        word_search = f.readlines()
        word_search = [line.strip('\n') for line in word_search]

    x_size = len(word_search[0])
    y_size = len(word_search)

    word_search = X_MASFinder(word_search)

    matches = 0
    for x in range(x_size):
        for y in range(y_size):
            matches += word_search.check_pos(x, y)

    print(f'There are {matches} X-MAS in the word search')


if __name__ == '__main__':
    puzzle_2('word_search.txt')
