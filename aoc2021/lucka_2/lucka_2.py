from typing import List, Tuple

FORWARD = "forward"
UP = "up"
DOWN = "down"


def parse_commands(commands: List[str]) -> Tuple[int, int]:
    depth = 0
    horizontal = 0
    for command in commands:
        direction, steps_str = command.split(" ")
        steps = int(steps_str)
        assert direction == FORWARD or direction == DOWN or direction == UP

        if direction == FORWARD:
            horizontal += steps
        elif direction == DOWN:
            depth += steps
        elif direction == UP:
            depth -= steps
    return depth, horizontal


def parse_commands_ex(commands: List[str]) -> Tuple[int, int]:
    aim = 0
    depth = 0
    horizontal = 0
    for command in commands:
        command_name, steps_str = command.split(" ")
        steps = int(steps_str)
        assert command_name == FORWARD or command_name == DOWN or command_name == UP

        if command_name == FORWARD:
            horizontal += steps
            depth += steps * aim
        elif command_name == DOWN:
            aim += steps
        elif command_name == UP:
            aim -= steps
    return depth, horizontal


if __name__ == "__main__":
    with open("./input.txt") as file:
        commands = file.readlines()
        depth, horizontal = parse_commands_ex(commands)
        print(f"Depth = {depth} and horizontal = {horizontal}")
        print(f"Multiplied = {depth * horizontal}")
