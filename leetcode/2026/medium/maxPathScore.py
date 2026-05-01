from typing import List


class Solution:
	def maxPathScore(self, grid: List[List[int]], k: int) -> int:
		n, m = len(grid), len(grid[0])
		NEG = -10**9
		dp = [[[NEG] * (k + 1) for _ in range(m)] for _ in range(n)]
		dp[0][0][0] = grid[0][0]
		for i in range(n):
			for j in range(m):
				cost_here = 1 if grid[i][j] > 0 else 0
				score_here = grid[i][j]
				for c in range(k+1):
					new_cost = c + cost_here
					if new_cost > k:
						continue
					if j > 0 and dp[i][j-1][c] != NEG:
						dp[i][j][new_cost] = max(dp[i][j][new_cost], dp[i][j-1][c] + score_here)
					if i > 0 and dp[i-1][j][c] != NEG:
						dp[i][j][new_cost] = max(dp[i][j][new_cost], dp[i-1][j][c] + score_here)
		max_path = max(dp[n-1][m-1])
		return max_path if max_path > 0 else -1



obj = Solution()
grid = [[0, 1],[1, 2]]
k = 1
print(obj.maxPathScore(grid, k))