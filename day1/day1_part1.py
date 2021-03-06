#!/usr/bin/env python

# Standard lib

# Third Party


def islarger(prev, new):
    if prev <= new:
        print("Decreased")
        return False
    else:
        print("increased")
        return True



def main():
    with open('input', 'r') as file:
        data = [int(line) for line in file.readlines()]

    increased = []
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


if __name__ == "__main__":
    main()
