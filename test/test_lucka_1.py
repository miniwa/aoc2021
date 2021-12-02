from aoc2021.lucka_1.main import calculate_increments, calculate_sliding_increments

example_input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def test_example_1():
    example_output_1 = [
        None,
        True,
        True,
        True,
        False,
        True,
        True,
        True,
        False,
        True
    ]
    output = calculate_increments(example_input)
    assert output == example_output_1


def test_example_2():
    example_output_2 = [
        None,
        True,
        False,
        False,
        True,
        True,
        True,
        True,
    ]
    output = calculate_sliding_increments(example_input)
    assert len(output) == len(example_output_2)
    assert output == example_output_2
