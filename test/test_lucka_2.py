from aoc2021.lucka_2.lucka_2 import parse_commands, parse_commands_ex

EXAMPLE_COMMANDS = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def test_example_1():
    depth, horizontal = parse_commands(EXAMPLE_COMMANDS)
    assert depth == 10
    assert horizontal == 15


def test_example_2():
    depth, horizontal = parse_commands_ex(EXAMPLE_COMMANDS)
    assert depth == 60
    assert horizontal == 15
