from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        visited = set()

        grid_rows = len(grid)
        grid_cols = len(grid[0])

        for row in range(grid_rows):
            for col in range(grid_cols):
                if grid[row][col] == 0:
                    q.append((row,col, 0))
                    visited.add((row,col))
        

        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        while q:
            curr_x, curr_y, dist = q.popleft()

            for dx,dy in directions:
                new_x = curr_x + dx
                new_y = curr_y + dy

                if new_x >= 0 and new_y >= 0 and new_x < grid_rows and new_y < grid_cols:
                    if (new_x, new_y) not in visited and grid[new_x][new_y] == ((1 << 31) - 1):
                        grid[new_x][new_y] = dist + 1
                        q.append((new_x,new_y,dist + 1))
                        visited.add((new_x,new_y))
