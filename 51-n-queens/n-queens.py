class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def backtrack(row, cols, diag1, diag2, current_board):
            # Base case: if all queens are placed, add the solution
            if row == n:
                result.append(["".join(row) for row in current_board])
                return
            
            # Try placing a queen in each column
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # Skip if the column or diagonal is attacked
                
                # Place the queen
                current_board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Recurse to place the next queen
                backtrack(row + 1, cols, diag1, diag2, current_board)
                
                # Backtrack: remove the queen and try the next column
                current_board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        result = []
        current_board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), current_board)
        return result