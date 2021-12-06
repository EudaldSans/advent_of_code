from typing import List

import numpy as np


class BingoBoard:
    def __init__(self, board: np.array):
        self._board = board
        self._number_track = np.zeros(board.shape, dtype=int)
        self._number_track.flags.writeable = True

        self.won = False
        self._last_draw = 0

    def new_number_drawn(self, number: int) -> bool:
        self._number_track[self._board == number] = 1

        completed_rows = np.prod(self._number_track, axis=0)
        completed_columns = np.prod(self._number_track, axis=1)

        self.won = (1 in completed_columns or 1 in completed_rows)
        self._last_draw = number

        return self.won

    def find_score(self) -> int:
        numbers_not_drawn = self._board - self._board*self._number_track

        return int(np.sum(numbers_not_drawn)) * self._last_draw

    def __str__(self):
        return str(self._board)

    @classmethod
    def new_board_from_str_list(cls, str_list: List[str]) -> 'BingoBoard':
        board_list = list()
        for row in str_list:
            new_row = row.rstrip().split(' ')
            new_row = [int(item) for item in new_row if item != '']

            board_list.append(new_row)

        return cls(np.array(board_list))


def main(path_to_bingo):
    with open(path_to_bingo) as bingo_file:
        bingo_str = bingo_file.readlines()

        number_draw = bingo_str.pop(0)
        number_draw = number_draw.rstrip().split(',')
        number_draw = list(map(int, number_draw))

        boards_data = bingo_str

    boards = list()

    while len(boards_data) > 0:
        _ = boards_data.pop(0)
        new_board = BingoBoard.new_board_from_str_list(boards_data[:5])
        boards_data = boards_data[5:]

        boards.append(new_board)

    winner_board = None
    loser_board = None
    boards_that_won = 0
    draw = -1

    for draw in number_draw:
        for board in boards:
            if board.won:
                continue

            if board.new_number_drawn(draw):
                boards_that_won += 1

                if winner_board is None:
                    winner_board = board

            if boards_that_won >= len(boards):
                loser_board = board
                break

    print(f'Last number drawn: {draw}')

    print(f'Winner board: ')
    print('-----------------')
    print(winner_board)
    print('-----------------')
    print(f'Score: {winner_board.find_score()}')

    print(f'Loser board: ')
    print('-----------------')
    print(loser_board)
    print('-----------------')
    print(f'Score: {loser_board.find_score()}')


if __name__ == '__main__':
    main('bingo.txt')


