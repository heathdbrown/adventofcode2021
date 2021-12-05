#!/usr/bin/env python


def parse_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data

def main():
    data = parse_file('input')
    number_pool =  [int(col.strip()) for col in data[0].split(',') ]

    # remove first line from file
    data.pop(0)

    # build the boards
    board_data = [tuple(int(num.strip()) for num in col.split() if num != '') for col in data ]

    boards = []
    for i, row in enumerate(board_data): 
        if len(row) == 0:
            board_start = i + 1
            board_end = i + 6
            #print(board_data[board_start:board_end])
            boards.append(board_data[board_start:board_end])

    # we got boards now we need to draw numbers
    #print(len(boards))
   
    for num in number_pool: 
        for board_num, board in enumerate(boards):
            for row_num, row in enumerate(board):
                if num in row:
                    print(f"{num} at [{board_num}][{row_num}][{row.index(num)}]")

    # I think you need to then generate a played board based on the found positions
    # Then we compare the two boards together to find the 'winner'

                    




if __name__ == "__main__":
    main()
