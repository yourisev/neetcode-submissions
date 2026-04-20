class Solution:

    def isValidRow(self, board: List[List[str]], i) -> bool:
        seen = set()
        row_dim = len(board[i])
        for j in range(row_dim):
            val = ord(board[i][j][0])
            if (board[i][j] != "." and (val - ord('1') < 0 or ord('9') - val < 0)) or val in seen :
                return False
            
            if board[i][j] != ".":
                seen.add(val)
        return True

    def isValidColumn(self, board: List[List[str]], i) -> bool:

        col_dim = len(board)
        seen = set()
        for j in range(col_dim):
            val = ord(board[j][i][0])
            if (board[j][i] != "." and (val - ord('1') < 0 or ord('9') - val < 0)) or val in seen :
                return False
            if board[j][i] != ".":
                seen.add(val)
        return True

    def isValidBox(self, board: List[List[str]], i) -> bool:
        col_start = (i%3) * 3
        col_end = col_start + 3
        row_start = (i//3) * 3
        row_end = row_start + 3
        i = row_start
        seen = set()

        while i >= row_start and i < row_end:
            j = col_start
            while j >= col_start and j < col_end:
                val = ord(board[i][j][0])
                if (board[i][j] != "." and (val - ord('1') < 0 or ord('9') - val < 0)) or val in seen :
                    return False
                if board[i][j] != ".":
                    seen.add(val)
                j+= 1
            i+= 1
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            if not self.isValidRow(board, i) or not self.isValidColumn(board, i) or not self.isValidBox(board, i):
                return False
        return True 