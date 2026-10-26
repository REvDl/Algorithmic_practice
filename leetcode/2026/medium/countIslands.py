from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        count_islands = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            curr = grid[r][c]
            grid[r][c] = 0
            return curr + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                res = dfs(r, c)
                if res != 0 and res % k == 0:
                    count_islands += 1
        return count_islands


obj = Solution()
grid =[[3,0,3,0], [0,3,0,3], [3,0,3,0]]
k = 3
print(obj.countIslands(grid, k))
