#!/usr/bin/env python

# Standard lib

# Third Party


def islarger(prev, new):
    if prev == new:
        print("no change")
        return True
    elif prev < new:
        print("decreased")
        return False
    else:
        print("increased")
        return True

def sumvalue(prev, cur, next_value):
    value = prev + cur + next_value

    return value
    
def review_measurements(data, increased=None, decreased=None):
    if increased is None:
        increased = []
    if decreased is None:
        decreased = []

    for i,num in enumerate(data):
        if i == 0:
            print("no previous measurement")
        else:
            prev = i - 1
            if islarger(data[prev], num):
                increased.append(num)
            else:
                decreased.append(num)
    print(f"Number of decreased: {len(decreased)}")


def main():
    with open('input', 'r') as file:
        data = [int(line) for line in file.readlines()]
    

    summed_measurements = []
    # sum of each 3 measurements
    for i,measure in enumerate(data):
        next_range = i + 3
        if len(data[i:next_range]) == 3:
            summed_measurements.append(sum(data[i:next_range]))

    review_measurements(summed_measurements)



if __name__ == "__main__":
    main()
