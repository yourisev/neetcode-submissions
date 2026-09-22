class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def traverse(grid, vis, row, col, rows, cols):

            visited.add((row,col))

            directions = [[-1,0], [1,0], [0,-1], [0,1]]

            for dx,dy in directions:
                new_x = row + dx
                new_y = col + dy

                if new_x >= 0 and new_y >= 0 and new_x < rows and new_y < cols:
                    if (new_x,new_y) not in vis and grid[new_x][new_y] == 'O':
                        traverse(grid, vis, new_x, new_y, rows, cols)

        visited = set()
        board_rows = len(board)
        board_cols = len(board[0])

        for i in range(board_rows):
            for j in range(board_cols):
                if (i,j) not in visited and (i in [0, board_rows - 1] or j in [0, board_cols - 1]) and board[i][j] == 'O':
                    traverse(board, visited, i, j, board_rows, board_cols)
        
        for i in range(board_rows):
            for j in range(board_cols):
                if (i,j) not in visited:
                    board[i][j] = 'X'