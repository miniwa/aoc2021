from aoc2021.lucka_3.lucka_3 import get_gamma_epsilon, get_oxygen_co2

EXAMPLE_INPUT = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]


def test_example_1_epsilon_gamma():
    gamma, epsilon = get_gamma_epsilon(EXAMPLE_INPUT)
    assert gamma == 22
    assert epsilon == 9


def test_example_2_oxygen_co2():
    oxygen, co2 = get_oxygen_co2(EXAMPLE_INPUT)
    assert oxygen == 23
    assert co2 == 10
