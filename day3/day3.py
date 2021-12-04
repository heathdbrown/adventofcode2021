#!/usr/bin/env python

from collections import Counter

# power_consumption --> gamma_rate * episilon rate
# gamma_rate -> binary --> most common bit --> decimal
# epsilon_rate --> binary --> least common bit --> decimal

def parse_file():
    with open('input', 'r') as file:
        #data = [tuple(int(bit) for bit in line.strip()) for line in file]

        # output: list of strings [ '1000001', '100001' ]
        data = [line.strip('\n') for line in file.readlines()]
    return data

def most_common_bit(data):
    most_common_bits = []

    # we just need to keep track of what bit(index) we are reviewing
    # build a list with the col that we are reviewing from the original list of numbers
    # Use Counter to pull the most_common and return the first value from the first tuple
    # return the list of all cols most_common_bits
    for i,k in enumerate(data[0]):
        bit = [number[i] for number in data]
        most_common_bits.append(Counter(bit).most_common()[0][0])

    return most_common_bits

def part1(data):
    gamma_bin = []
    episilon_bin = []
    for i,k in enumerate(data[0]):
        bit = [number[i] for number in data]
        # use counter to return the first value, from the first list, first tuple
        # and add to list
        gamma_bin.append(Counter(bit).most_common(1)[0][0])
        # use counter to return the last value from list first value
        # and add to list
        episilon_bin.append(Counter(bit).most_common()[-1][0])

    # join list together using .join which takes an interable
    # use int(str, 2) to convert each string into a decimal integer from binary
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
    # we need to interate over each col, and find the most_common_bit
    # we need to then store all the numbers that match the most_common_bit in that col
    # we then interate over these values and find the most_common_bit
    # we need to store all numbers that match the most_common_bit in the col or if equally common
    # keep values with 1 in the position being considered


def main():
    data = parse_file()
    #part1(data)
    part2(data)

if __name__ == "__main__":
    main()
