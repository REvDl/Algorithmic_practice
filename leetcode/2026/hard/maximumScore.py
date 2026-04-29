from typing import List


class Solution:
	def maximumScore_BAD(self, grid: List[List[int]]) -> int:
		n, m = len(grid), len(grid[0])
		dp = [[[0] * 3 for _ in range(n + 1)] for _ in range(n + 1)]
		prefix_sum = [[0] * m for _ in range(n + 1)]
		for i in range(m):
			for j in range(n):
				prefix_sum[j + 1][i] = prefix_sum[j][i] + grid[j][i]
		for i in range(n):
			for j in range(n+1):
				for x in range(n+1):
					if i == 0:
						dp[0][x][0] = 0
						dp[0][x][1] = 0
						dp[0][x][2] = 0
						continue
					if j > x:
						profit = prefix_sum[j][i] - prefix_sum[x][i]
						dp[i][x][1] = max(dp[i][x][1], max(dp[i-1][j]) + profit)
					elif j < x:
						profit = prefix_sum[x][i-1] - prefix_sum[j][i-1]
						dp[i][x][0] = max(dp[i][x][0], max(dp[i-1][j][0], dp[i-1][j][2]) + profit)
					else:
						dp[i][x][2] = max(dp[i][x][2], max(dp[i-1][j]))
		return max(state for row in dp[n-1] for state in row)



	def maximumScore_im_bussy_help_me_please(self, grid: List[List[int]]) -> int:
		n, m = len(grid), len(grid[0])
		prefix_sum = [[0] * m for _ in range(n + 1)]
		dp = [[0, 0] for _ in range(n + 1)]
		for j in range(n):
			new_dp = [[0, 0] for _ in range(n + 1)]
			for h in range(n + 1):
				for h_prev in range(n + 1):
					score = 0
					if j > 0 and h > h_prev:
						score = prefix_sum[j - 1][h] - prefix_sum[j - 1][h_prev]
					new_dp[h][0] = max(new_dp[h][0], dp[h_prev][0] + score)
			for h in range(n + 1):
				for h_prev in range(n + 1):
					score = 0
					if h < h_prev:
						score = prefix_sum[j][h_prev] - prefix_sum[j][h]
					new_dp[h][1] = max(new_dp[h][1], max(dp[h_prev]) + score)
			dp = new_dp
		return max(max(row) for row in dp)

	def maximumScore(self, grid: List[List[int]]) -> int:
		n = len(grid)
		dp0 = [0] * (n + 1)
		dp1 = [0] * (n + 1)
		for j in range(1, n):
			new_dp0 = [0] * (n + 1)
			new_dp1 = [0] * (n + 1)
			for i in range(n + 1):
				prev = 0
				curr = sum(grid[x][j] for x in range(i))
				for y in range(n + 1):
					if y > 0 and y <= i:
						curr -= grid[y - 1][j]
					if j > 0 and y > i:
						prev += grid[y - 1][j - 1]
					new_dp0[y] = max(new_dp0[y], prev + dp0[i], dp1[i])
					new_dp1[y] = max(new_dp1[y], curr + dp1[i], curr + prev + dp0[i])
			dp0, dp1 = new_dp0, new_dp1
		return max(dp1)


obj = Solution()
grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]
print(obj.maximumScore(grid))