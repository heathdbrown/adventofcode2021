#!/usr/bin/env python

from collections import Counter

# power_consumption --> gamma_rate * episilon rate
# gamma_rate -> binary --> most common bit --> decimal
# epsilon_rate --> binary --> least common bit --> decimal

def parse_file():
    with open('input', 'r') as file:
        data = [line.strip('\n') for line in file.readlines()]
    return data

def most_common_bit(data):
    most_common_bits = []
    for i,k in enumerate(data[0]):
        bit = [number[i] for number in data]
        most_common_bits.append(Counter(bit).most_common()[0][0])

    return most_common_bits

def part1(data):
    gamma_bin = []
    episilon_bin = []
    for i,k in enumerate(data[0]):
        bit = [number[i] for number in data]
        gamma_bin.append(Counter(bit).most_common(1)[0][0])
        episilon_bin.append(Counter(bit).most_common()[-1][0])
    gamma_rate = int("".join(gamma_bin), 2)
    episilon_rate = int("".join(episilon_bin), 2)
    print(gamma_rate)
    print(episilon_rate)
    print(f"Total: {gamma_rate * episilon_rate}")


def part2(data):
    """
    oxygen_generator_rating
    co2_scrubber_rating
    total = oxygen_generator_rating * c02_scrubber_rating
    """
    most_common_bits = most_common_bit(data)
    print(most_common_bits)
    match_num_1 = []
    
    for i,k in enumerate(data[0]):
        for number in data:
            for bit in most_common_bits:
                if bit == number[i]:
                    print(f"{bit}, {number}")

    print(len(match_num_1))


def main():
    data = parse_file()
    part1(data)
    #part2(data)

if __name__ == "__main__":
    main()
