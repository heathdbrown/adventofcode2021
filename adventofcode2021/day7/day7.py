#!/usr/bin/env python

import statistics

def parse_file(file_name):
    with open(file_name, 'r') as file:
        data = [int(i) for i in file.readline().split(',')]
    return data

def fuel_consumption(pos, movement):
    move = pos - movement
    return abs(move)*(abs(move)+1)//2

def main():
    data = parse_file('input')
    crabs = len(data)
    sum_positions = sum(data)
    avg_position = round(sum_positions // crabs)
    median_position = statistics.median(sorted(data))
    print(avg_position)
    print(sum_positions / crabs)
    fuel_used = sum([fuel_consumption(i, avg_position) for i in data])
    print(fuel_used)


if __name__ == "__main__":
    main()
