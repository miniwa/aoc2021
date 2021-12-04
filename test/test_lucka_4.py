from aoc2021.lucka_4.lucka_4 import parse_input, get_first_winning_board, get_last_winning_board

EXAMPLE_INPUT = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "\n",
    "22 13 17 11  0",
    "8  2 23  4 24",
    "21  9 14 16  7",
    "6 10  3 18  5",
    "1 12 20 15 19",
    "",
    "3 15  0  2 22",
    "9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    "2  0 12  3  7",
]


def test_example_1_parse_input():
    bingo_sequence, boards = parse_input(EXAMPLE_INPUT)
    assert bingo_sequence == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3,
                              26, 1]
    assert len(boards) == 3
    first = boards[0]
    rows = first.get_rows()
    assert rows == [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ]

    columns = first.get_columns()
    assert columns[0] == [22, 8, 21, 6, 1]
    assert columns[1] == [13, 2, 9, 10, 12]
    assert columns[2] == [17, 23, 14, 3, 20]
    assert columns[3] == [11, 4, 16, 18, 15]
    assert columns[4] == [0, 24, 7, 5, 19]


def test_example_1_first_winning_sequence():
    bingo_seq, boards = parse_input(EXAMPLE_INPUT)
    winning_seq, winning_board = get_first_winning_board(bingo_seq, boards)
    assert len(winning_seq) == 12
    assert winning_board.get_rows() == boards[2].get_rows()
    assert winning_board.get_columns() == boards[2].get_columns()

    score = winning_board.get_winning_score(winning_seq)
    assert score == 4512


def test_example_2():
    bingo_seq, boards = parse_input(EXAMPLE_INPUT)
    seq, winner = get_last_winning_board(bingo_seq, boards)
    score = winner.get_winning_score(seq)
    assert score == 1924
