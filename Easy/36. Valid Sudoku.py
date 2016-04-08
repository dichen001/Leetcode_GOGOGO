"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        sudoku = set()
        for i,row in enumerate(board):
            for j,num in enumerate(row):
                if num == '.':
                    continue
                seen = [(i,num),(num,j),(i/3,j/3,num)]
                for unique in seen:
                    if unique in sudoku:
                        return False
                    else:
                        sudoku.add(unique)
        return True