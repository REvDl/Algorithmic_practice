from typing import List



class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        grid_flat = [0 for _ in range(n) for _ in range(m)]
        idx = 0
        for i in range(n):
            for j in range(m):
                idx = (i * m + j + k) % (n * m)
                grid_flat[idx] = grid[i][j]
        matrix = [grid_flat[i:i+m] for i in range(0, len(grid_flat), m)]
        return matrix




obj = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(obj.shiftGrid(grid, k))
