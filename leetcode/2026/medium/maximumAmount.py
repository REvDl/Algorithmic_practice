from typing import List


class Solution:
	def maximumAmount(self, coins: List[List[int]]) -> int:
		INF = 10 ** 5
		m, n = len(coins), len(coins[0])
		dp = [[[-INF] * 3 for _ in range(n)] for _ in range(m)]
		dp[0][0][0] = coins[0][0]
		dp[0][0][1] = max(0, coins[0][0])
		dp[0][0][2] = max(0, coins[0][0])

		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0: continue
				if i > 0:
					dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][0] + coins[i][j])
					dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][1] + coins[i][j], dp[i - 1][j][0])
					dp[i][j][2] = max(dp[i][j][2], dp[i - 1][j][2] + coins[i][j], dp[i - 1][j][1])
				if j > 0:
					dp[i][j][0] = max(dp[i][j][0], dp[i][j - 1][0] + coins[i][j])
					dp[i][j][1] = max(dp[i][j][1], dp[i][j - 1][1] + coins[i][j], dp[i][j - 1][0])
					dp[i][j][2] = max(dp[i][j][2], dp[i][j - 1][2] + coins[i][j], dp[i][j - 1][1])
		return max(dp[m-1][n-1][0], dp[m-1][n-1][1], dp[m-1][n-1][2])





obj = Solution()
TESTS = [[[0,1,-1],[1,-2,3],[2,-3,4]], [[10,10,10],[10,10,10]], [[-7,12,12,13],[-6,19,19,-6],[9,-2,-10,16],[-4,14,-10,-9]]]
EXPECTED = [8, 40, 60]
for i in range(len(TESTS)):
	print(f"{TESTS[i]}\n{obj.maximumAmount(TESTS[i])} \nExpected: {EXPECTED[i]}")