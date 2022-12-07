#!/usr/bin/env python


# aim
# forword increase horizontoal_position
#   increase horizontal_pos by X units
#   increase depth by your aim multiplied by X
# down increases aim
# up decrease aim


def main():
    horizontal_pos = 0
    depth = 0
    aim = 0

    with open('input', 'r') as file:
        data = [line.split() for line in file.readlines()]

    for instruction in data:
        if instruction[0] == "forward":
            horizontal_pos += int(instruction[1])
            depth += int(instruction[1]) * aim
        if instruction[0] == "down":
            aim += int(instruction[1])
        if instruction[0] == "up":
            aim -= int(instruction[1])

    print(f"horizontal postion: {horizontal_pos}, depth: {depth}")
    print(f"Total: {horizontal_pos * depth}")

if __name__ == "__main__":
    main()
