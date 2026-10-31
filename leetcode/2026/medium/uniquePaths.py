from typing import List



class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        R = [[0] * (cols + 1) for _ in range(rows + 1)]
        D = [[0] * (cols + 1) for _ in range(rows + 1)]
        R[0][0] = 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    total = R[i][j] + D[i][j]
                    R[i][j+1] += total
                    D[i+1][j] += total
                else:
                    d_el = D[i][j]
                    r_el = R[i][j]
                    R[i][j+1] += d_el
                    D[i+1][j] += r_el
        return (R[rows-1][cols-1] + D[rows-1][cols-1]) % (10 ** 9 + 7)

obj = Solution()
grid = [[0,1,0],[0,0,1],[1,0,0]]
print(obj.uniquePaths(grid))
