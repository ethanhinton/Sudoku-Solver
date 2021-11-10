from random import randint as rand

class Board:

    def __init__(self, board=False):
        self.board = ([[0 for i in range(9)] for j in range(9)] if not board else board)
        
        if not board:
            self.fill_board()


    # Lets user fill board up row by row, checking if it is valid at each step
    def fill_board(self):
        print("Fill the board by typing in numbers 1-9 in spaces of your choice!")       
        for i in range(9):
            self.print_board()
            for j in range(9):
                while True:
                    try:
                        num = int(input(f'Input the next number in the row (element {j}) : '))
                        if num < 1 or num > 9:
                            raise ValueError
                    except:
                        print('Please enter a number between 1 and 9')

                    if self.is_legal(num, i, j) or num == 0:
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

    def print_board(self, initial=False):
        
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
    
    def solve(self):
        try:
            i, j = self.find_empty()
        except TypeError:
            return True

        for num in range(1, 10):
            if self.is_legal(num, i, j):
                self.board[i][j] = num
                if self.solve():
                    return True
            self.board[i][j] = 0
        
        return False
        
    
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j

        return False


if __name__ == '__main__':

    board = [
        [0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0],
        [1,9,0,0,0,4,5,0,0],
        [8,2,0,1,0,0,0,4,0],
        [0,0,4,6,0,2,9,0,0],
        [0,5,0,0,0,3,0,2,8],
        [0,0,9,3,0,0,0,7,4],
        [0,4,0,0,5,0,0,3,6],
        [7,0,3,0,1,8,0,0,0]
    ]
    sudoku = Board(board)
    print('Initial Board is : \n')
    sudoku.print_board()
    sudoku.solve()
    print('')
    print('Solved board is : \n')
    sudoku.print_board()
