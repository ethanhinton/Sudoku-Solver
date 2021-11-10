from random import randint as rand

class Board:

    def __init__(self, number=1):
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.fill_board(number)

    
    def fill_board(self, number):        
        for pos in range(number):
            while True:
                i = rand(0,8)
                j = rand(0,8)

                if self.board[i][j] == 0:
                    self.board[i][j] = rand(1,9)
                    break
                

    def print(self):
        print(self.board)
    
sudoku = Board(number=5)
sudoku.print()