class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def traverse(grid, vis, x, y, r_size, c_size):

            directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

            for dx,dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x >= 0 and new_y >= 0 and new_x < r_size and new_y < c_size:
                    if (new_x, new_y) not in vis and grid[new_x][new_y] == '1':
                        vis.add((new_x, new_y))
                        traverse(grid, vis, new_x, new_y, r_size, c_size)



        visited = set()
        grid_rows = len(grid)
        grid_cols = len(grid[0])
        count_islands = 0

        for x_pos in range(grid_rows):
            for y_pos in range(grid_cols):
                if (x_pos,y_pos) not in visited and grid[x_pos][y_pos] == '1':
                    visited.add((x_pos,y_pos))
                    traverse(grid, visited, x_pos, y_pos, grid_rows, grid_cols)
                    count_islands += 1
        
        return count_islands
        