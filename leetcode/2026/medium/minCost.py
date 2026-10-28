


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0] = {grid[0][0]}
        for j in range(1, n):
            for val in dp[0][j-1]:
                dp[0][j].add(val ^ grid[0][j])
        
        for i in range(1, m):
            for val in dp[i-1][0]:
                dp[i][0].add(val ^ grid[i][0])
        

        for i in range(1, m):
            for j in range(1, n):
                possible_prev_xors = dp[i-1][j] | dp[i][j-1]
                for prev_xor in possible_prev_xors:
                    current_xor = prev_xor ^ grid[i][j]
                    dp[i][j].add(current_xor)
        return min(dp[m-1][n-1])

obj = Solution()
grid = [[1,2],[3,4]]
print(obj.minCost(grid))
