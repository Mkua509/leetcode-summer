class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Check rows
        for rows in range(9):
            seen = set()
            for i in range(9):
                if board[rows][i] == ".":
                    continue
                if board[rows][i] in seen:
                    return False
                seen.add(board[rows][i])
        
        # Check cols
        for cols in range(9):
            seen = set()
            for i in range(9):
                if board[i][cols] == ".":
                    continue
                if board[i][cols] in seen:
                    return False
                seen.add(board[i][cols])

        # Check squares
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True