#https://leetcode.com/problems/valid-sudoku/

def isValidSudoku(board):
    seen = sum(([(c, i), (j, c), (int(i/3), int(j/3), c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'), [])
    return len(seen) == len(set(seen))
