class Solution:

    def row_verification(self, board: List[List[str]], pos:int):
        seen = set()
        for i in range(len(board[pos])):
            if board[pos][i] in seen:
                return False
            else:
                if board[pos][i] != ".":
                    seen.add(board[pos][i])
        
        return True
    
    def column_verification(self, board: List[List[str]], pos:int):
        seen = set()
        for i in range(len(board)):
            if board[i][pos] in seen:
                return False
            else:
                if board[i][pos] != ".":
                    seen.add(board[i][pos])
        
        return True
    
    def box_verification(self, board: List[List[str]], pos:int):
        seen = set()
        start_row = (pos // 3) * 3
        end_row = start_row + 3
        start_col = (pos % 3) * 3
        end_col = start_col + 3

        i = start_row

        while i < end_row:
            j = start_col
            while j < end_col:
                if board[i][j] in seen:
                    return False
                else:
                    if board[i][j] != ".":
                        seen.add(board[i][j])
                j += 1
            i += 1
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        result = True
        for i in range(len(board)):
            result = result and self.row_verification(board,i)
            if not result:
                return result
            result = result and self.column_verification(board,i)
            if not result:
                return result
            result = result and self.box_verification(board,i)
        
        return result    