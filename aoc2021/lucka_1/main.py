from typing import List


def calculate_increments(depth_sequence: List[int]):
    output_sequence = []
    last_number = None
    for number in depth_sequence:
        if last_number is None:
            output_sequence.append(None)
        elif number > last_number:
            output_sequence.append(True)
        else:
            output_sequence.append(False)
        last_number = number
    return output_sequence


def calculate_sliding_increments(depth_sequence: List[int]):
    res = []
    prev_sum = None
    for index in range(2, len(depth_sequence)):
        slide = depth_sequence[index - 2: index + 1]
        assert len(slide) == 3

        _sum = sum(slide)
        if prev_sum is None:
            res.append(None)
        elif _sum > prev_sum:
            res.append(True)
        else:
            res.append(False)
        prev_sum = _sum
    return res


if __name__ == "__main__":
    _input = []
    with open("./input.txt") as f:
        for line in f.readlines():
            parsed_number = int(line)
            _input.append(parsed_number)

    output = calculate_increments(_input)
    assert len(_input) == len(output)

    where_number_increased = [flag for flag in output if flag is True]
    print("Number of increments: ", len(where_number_increased))

    output_sliding = calculate_sliding_increments(_input)
    where_sum_increased = [flag for flag in output_sliding if flag is True]
    print("Number of sliding sums that increased: ", len(where_sum_increased))
