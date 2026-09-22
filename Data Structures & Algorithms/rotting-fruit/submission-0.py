from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        visited = set()

        grid_rows = len(grid)
        grid_cols = len(grid[0])
        cnt_fresh = 0

        for row in range(grid_rows):
            for col in range(grid_cols):
                if grid[row][col] == 2:
                    q.append((row,col,0))
                    visited.add((row,col))
                elif grid[row][col] == 1:
                    cnt_fresh += 1
        

        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        time = 0

        while q:
            curr_x, curr_y, tm = q.popleft()

            for dx,dy in directions:
                new_x = curr_x + dx
                new_y = curr_y + dy

                if new_x >= 0 and new_y >= 0 and new_x < grid_rows and new_y < grid_cols:
                    if (new_x, new_y) not in visited and grid[new_x][new_y] == 1:
                        cnt_fresh -= 1
                        visited.add((new_x, new_y))
                        q.append((new_x, new_y, tm + 1))

            time = tm

        return -1 if cnt_fresh > 0 else time
