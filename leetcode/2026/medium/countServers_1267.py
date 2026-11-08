

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])
        res = 0
        cols_with_ones = [sum(col) for col in zip(*grid)]
        row_has_one = [sum(row) for row in grid]
        for i in range(len(grid)):
            for j in range(c):
                if grid[i][j] == 1 and (row_has_one[i] > 1 or cols_with_ones[j] > 1):
                    res += 1
        return res

obj = Solution()
grid = [[[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]], [[1,0],[1,1]], [[1,0],[0,1]]]
for arr in grid:
    print(obj.countServers(arr))
