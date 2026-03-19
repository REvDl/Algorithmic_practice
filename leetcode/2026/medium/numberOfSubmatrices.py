from typing import List


class Solution:
	def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
		rows, cols = len(grid), len(grid[0])
		result = 0
		dp = [[ [0, 0] for _ in range(cols+1)] for _ in range(rows+1)]
		for i in range(rows):
			for j in range(cols):
				current_sum = 1 if grid[i][j] == "X" else (-1 if grid[i][j] == "Y" else 0)
				has_x = 1 if grid[i][j] == "X" else 0
				dp[i][j][0] = current_sum + dp[i-1][j][0] + dp[i][j-1][0] - dp[i-1][j-1][0]
				dp[i][j][1] = has_x | dp[i - 1][j][1] | dp[i][j - 1][1]
				if dp[i][j][0] == 0 and dp[i][j][1]:
					result += 1
		return result