"""
Recursive Brute-Force Sudoku Solver

accepts sudoku puzzles in text form
9 lines of 9 numbers, empty spaces indicated
as 0

comes packaged with a very challenging sudoku puzzle from
the expert section of sudoku.com
"""


# building the board array from the puzzle file
puzzle_file = 'puzzle.sdk'
board = []
with open(puzzle_file) as puzzle_file:
    lines = puzzle_file.readlines()
    i = 0
    for line in lines:
        board.append([])
        for j in range(9):
            board[i].append(int(line[j]))
        i += 1
        
def print_board(array):
    """
    an alternative to numpy matrix printing
    """
    for x in range(len(array)):
        for y in range(len(array[0])):
            print(array[x][y], end =' ')
        print()
    print()

def evaluate_cell(board,x,y):
    """
    returns a list cell's possible moves
    """
    possible_moves = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        try:
            possible_moves.remove(board[x][i])
        except ValueError:
            pass
        try:
            possible_moves.remove(board[i][y])
        except ValueError:
            pass
    # some arithmetic to calculate the 3x3 quandrant a
    # cell "lives" in
    q = ( x//3, y//3 )
    for i in range(q[0]*3, q[0]*3+3):
        for j in range(q[1]*3, q[1]*3+3):
            try:
                possible_moves.remove(board[i][j])
            except ValueError:
                pass      
    return possible_moves
       

def solution(board):
    """
    recursively solves the board by looping through each cell's
    possible moves. Prints the solution, if no solution is possible the program
    will terminate without any output.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                possible_moves = evaluate_cell(board,i,j)
                for move in possible_moves:
                    board[i][j] = move
                    solution(board)
                    # if the solution does not succeed, set this
                    # cell back to zero
                    board[i][j] = 0
                # and return to the cell being last iterated
                return
    # upon all recursive funny business being completed,
    # print the final board
    print_board(board)
    
solution(board)