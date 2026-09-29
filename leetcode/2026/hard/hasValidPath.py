from collections import deque
from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        @cache
        def dfs(r, c, current_count_brace):
            if current_count_brace < 0:
                return False
            if r == rows - 1 and c == cols - 1:
                return current_count_brace == 0
            if r + 1 < rows:
                if dfs(r + 1, c, current_count_brace + (1 if grid[r + 1][c] == "(" else - 1)):
                    return True
            if c + 1 < cols:
                if dfs(r, c + 1, current_count_brace + (1 if grid[r][c + 1] == "(" else - 1)):
                    return True
            return False
        if grid[0][0] == ")":
            return False
        return dfs(0, 0, 1)




obj = Solution()
grid = [[")"]]
print(obj.hasValidPath(grid))
