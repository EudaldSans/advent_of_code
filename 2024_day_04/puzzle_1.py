from typing import List


class WordFinder:
    def __init__(self, word_search: List[str], word_to_search: str):
        self.word_search = word_search
        self.word_to_search = word_to_search
        self.word_len = len(word_to_search)

        self.x_size = len(word_search[0])
        self.y_size = len(word_search)

    def find_0_deg(self, x: int, y: int) -> str:
        return ''.join([self.word_search[y][x + a] for a in range(self.word_len) if (x + a) < self.x_size])

    def find_45_deg(self, x: int, y: int) -> str:
        return ''.join([self.word_search[y + a][x + a] for a in range(self.word_len)
                        if (x + a) < self.x_size and (y + a) < self.y_size])

    def find_90_deg(self, x: int, y: int) -> str:
        return ''.join([self.word_search[y + a][x] for a in range(self.word_len) if (y + a) < self.y_size])

    def find_135_deg(self, x: int, y: int) -> str:
        return ''.join([self.word_search[y + a][x - a] for a in range(self.word_len)
                        if (x - a) >= 0 and (y + a) < self.y_size])

    def find_180_deg(self, x: int, y: int) -> str:
        return ''.join([self.word_search[y][x - a] for a in range(self.word_len) if (x - a) >= 0])

    def find_225_deg(self, x: int, y: int) -> str:
        return ''.join([self.word_search[y - a][x - a] for a in range(self.word_len)
                        if (x - a) >= 0 and (y - a) >= 0])

    def find_270_deg(self, x: int, y: int) -> str:
        return ''.join([self.word_search[y - a][x] for a in range(self.word_len) if (y - a) >= 0])

    def find_315_deg(self, x: int, y: int) -> str:
        return ''.join([self.word_search[y - a][x + a] for a in range(self.word_len)
                        if (x + a) < self.x_size and (y - a) >= 0])

    def check_pos(self, x: int, y: int) -> int:
        if x >= self.x_size or y >= self.y_size:
            raise ValueError()

        if self.word_search[y][x] != self.word_to_search[0]:
            return 0

        matches = 0

        if self.find_0_deg(x, y) == self.word_to_search: matches += 1
        if self.find_45_deg(x, y) == self.word_to_search: matches += 1
        if self.find_90_deg(x, y) == self.word_to_search: matches += 1
        if self.find_135_deg(x, y) == self.word_to_search: matches += 1
        if self.find_180_deg(x, y) == self.word_to_search: matches += 1
        if self.find_225_deg(x, y) == self.word_to_search: matches += 1
        if self.find_270_deg(x, y) == self.word_to_search: matches += 1
        if self.find_315_deg(x, y) == self.word_to_search: matches += 1

        return matches


def main(word_search_file: str):
    with open(word_search_file, 'r') as f:
        word_search = f.readlines()
        word_search = [line.strip('\n') for line in word_search]

    x_size = len(word_search[0])
    y_size = len(word_search)

    word_search = WordFinder(word_search, 'XMAS')

    matches = 0
    for x in range(x_size):
        for y in range(y_size):
            matches += word_search.check_pos(x, y)

    print(f'There are {matches} occurrences of the word XMAS in the word search')


if __name__ == '__main__':
    main('word_search.txt')
