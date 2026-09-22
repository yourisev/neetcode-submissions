class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def traverse(grid, vis, path_vis, x, y, r_size, c_size):

            vis.add((x,y))
            path_vis.append((x,y))

            directions = [[-1,0], [1,0], [0,-1], [0,1]]

            for dx,dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x >= 0 and new_y >= 0 and new_x < r_size and new_y < c_size:
                    if (new_x, new_y) not in vis and grid[new_x][new_y] == 1:
                        traverse(grid, vis, path_vis, new_x, new_y, r_size, c_size)


        visited = set()
        grid_rows = len(grid)
        grid_cols = len(grid[0])
        area = 0

        for x_pos in range(grid_rows):
            for y_pos in range(grid_cols):
                if (x_pos,y_pos) not in visited and grid[x_pos][y_pos] == 1:
                    path_visited = []
                    traverse(grid, visited, path_visited, x_pos, y_pos, grid_rows, grid_cols)
                    area = max(area,len(path_visited))
        
        return area