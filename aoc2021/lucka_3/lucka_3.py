from typing import List


def to_dec(number: str):
    _len = len(number)
    decimal = 0
    for i in range(_len):
        pos = _len - 1 - i
        if number[i] == "1":
            decimal += 2**pos
    return decimal


def count_bits(index: int, numbers: List[str]):
    count_1 = 0
    count_0 = 0
    for number in numbers:
        if number[index] == "1":
            count_1 += 1
        elif number[index] == "0":
            count_0 += 1
    return count_1, count_0


def get_gamma_epsilon(numbers: List[str]):
    char_count = len(numbers[0])
    gamma = 0
    epsilon = 0
    for index in range(char_count):
        count_1, count_0 = count_bits(index, numbers)
        assert count_1 != count_0

        pos = char_count - 1 - index
        number = 2 ** pos
        if count_1 > count_0:
            gamma += number
        else:
            epsilon += number
    return gamma, epsilon


def filter_by_pos(numbers: List[str], compare_func):
    char_count = len(numbers[0])
    _copy = [number for number in numbers]

    for index in range(char_count):
        count_1, count_0 = count_bits(index, _copy)
        bit = compare_func(count_1, count_0)
        _copy = [number for number in _copy if number[index] == bit]
        if len(_copy) == 1:
            return _copy[0]
    assert len(_copy) == 1
    return _copy[0]


def get_oxygen_co2(numbers: List[str]):
    def _oxygen_compare(count_1, count_0):
        return "1" if count_1 >= count_0 else "0"

    def _co2_compare(count_1, count_0):
        return "0" if count_0 <= count_1 else "1"

    oxygen = filter_by_pos(numbers, _oxygen_compare)
    co2 = filter_by_pos(numbers, _co2_compare)
    return to_dec(oxygen), to_dec(co2)


def main():
    with open("./input.txt") as file:
        numbers = file.readlines()
        numbers = [line.strip() for line in numbers]

    gamma, epsilon = get_gamma_epsilon(numbers)
    print(f"Gamma * Epsilon = {gamma * epsilon}")

    oxygen, co2 = get_oxygen_co2(numbers)
    print(f"Oxygen * CO2 = {oxygen * co2}")


if __name__ == "__main__":
    main()
