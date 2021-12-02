#!/usr/bin/env python



# forword increase horizontoal_position
# down increases depth
# up decrease depth


def main():
    horizontal_pos = 0
    depth = 0

    with open('input', 'r') as file:
        data = [line.split() for line in file.readlines()]

    for instruction in data:
        if instruction[0] == "forward":
            horizontal_pos += int(instruction[1])
        if instruction[0] == "down":
            depth += int(instruction[1])
        if instruction[0] == "up":
            depth -= int(instruction[1])

    print(f"horizontal postion: {horizontal_pos}, depth: {depth}")
    print(f"Total: {horizontal_pos * depth}")

if __name__ == "__main__":
    main()
