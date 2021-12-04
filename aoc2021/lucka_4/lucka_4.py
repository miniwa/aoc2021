from typing import List
from py_linq import Enumerable


class Board:
    def __init__(self, numbers: List[int]):
        assert len(numbers) == 5 * 5
        self._numbers = numbers

    def get_rows(self):
        rows = []
        for index in range(0, len(self._numbers), 5):
            rows.append(self._numbers[index: index + 5])
        assert len(rows) == 5
        return rows

    def get_columns(self):
        columns = []
        for index in range(0, 5):
            columns.append([
                self._numbers[index + 0 * 5],
                self._numbers[index + 1 * 5],
                self._numbers[index + 2 * 5],
                self._numbers[index + 3 * 5],
                self._numbers[index + 4 * 5],
            ])
        assert len(columns) == 5
        return columns

    def is_winner(self, bingo_sequence: List[int]):
        _combinations = Enumerable(self.get_rows() + self.get_columns())
        for combination in _combinations:
            for number in combination:
                if number not in bingo_sequence:
                    break
            else:
                return True
        return False

    def get_winning_score(self, winning_seq: List[int]):
        unmarked = [number for number in self._numbers if number not in winning_seq]
        unmarked_sum = sum(unmarked)
        return unmarked_sum * winning_seq[-1]


def number_line_to_int(number_line: str) -> List[int]:
    numbers = []
    for number in number_line.split():
        numbers.append(int(number))
    return numbers


def parse_input(lines: List[str]):
    iterator = iter(lines)
    boards = []
    bingo_sequence = list(map(lambda x: int(x), next(iterator).split(",")))
    for line in iterator:
        if line.strip() == "":
            board_numbers = (number_line_to_int(next(iterator)) +
                             number_line_to_int(next(iterator)) +
                             number_line_to_int(next(iterator)) +
                             number_line_to_int(next(iterator)) +
                             number_line_to_int(next(iterator)))
            assert len(board_numbers) == 5 * 5
            boards.append(Board(board_numbers))
    return bingo_sequence, boards


def get_first_winning_board(bingo_sequence: List[int], boards: List[Board]):
    for index in range(len(bingo_sequence)):
        seq_part = bingo_sequence[0: index + 1]
        for board in boards:
            if board.is_winner(seq_part):
                return seq_part, board


def get_last_winning_board(bingo_sequence: List[int], boards: List[Board]):
    _len = len(bingo_sequence)
    _boards = [board for board in boards]
    for index in range(_len):
        seq_part = bingo_sequence[0: index + 1]
        for board in _boards:
            if board.is_winner(seq_part):
                _boards.remove(board)
                if len(_boards) == 0:
                    return seq_part, board


def main():
    with open("./input.txt") as file:
        lines = file.readlines()
    bingo_seq, boards = parse_input(lines)
    winning_seq, winner = get_first_winning_board(bingo_seq, boards)
    score = winner.get_winning_score(winning_seq)
    print(f"First winner score = {score}")

    last_seq, last_winner = get_last_winning_board(bingo_seq, boards)
    last_winner_score = last_winner.get_winning_score(last_seq)
    print(F"Last winner score = {last_winner_score}")


if __name__ == "__main__":
    main()

