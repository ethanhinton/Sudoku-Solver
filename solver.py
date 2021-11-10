from random import randint as rand

class Board:

    def __init__(self, number=1):
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.fill_board(number)

    # Fills board with a specified amount of non-zero numbers if legal
    # Avoid setting number too high as this will create lots of cases where the number is illegal
    def fill_board(self, number):        
        for pos in range(number):
            while True:
                i = rand(0,8)
                j = rand(0,8)

                if self.board[i][j] == 0:
                    num = rand(1,9)
                    if self.is_legal(num, i, j):
                        self.board[i][j] = num
                        break
    
    def is_legal(self, number, row, column):
        
        #check row
        for i in range(9):
            if self.board[row][i] == number and i != column:
                return False
        
        #check column
        for i in range(9):
            if self.board[i][column] == number and i != row:
                return False
        
        #check box
        box_x = column // 3
        box_y = row // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == number and i != row and j != column:
                    return False
        
        return True

    def print_board(self):
        for ind, row in enumerate(self.board):
            if ind % 3 == 0 and ind != 0:
                print("-----------------------")
            for i in range(9):
                if i % 3 == 0 and i != 0:
                    print(f' | {row[i]}', end="")
                elif i == 8:
                    print(f' {row[i]}')
                else:
                    print(f' {row[i]}', end="")
            
    
sudoku = Board(number=20)
sudoku.print_board()