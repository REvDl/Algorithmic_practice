from typing import List


class Solution:
	def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
		n, m = len(robot), len(factory)
		dp = [[float("inf") for _ in range(n + 1)] for _ in range(m + 1)]
		robot.sort()
		factory.sort()
		dp[0][0] = 0
		for i in range(m):
			for j in range(n + 1):
				dist = 0
				dp[i + 1][j] = dp[i][j]
				for k in range(1, min(j, factory[i][1]) + 1):
					dist += abs(robot[j - k] - factory[i][0])
					dp[i + 1][j] = min(dist + dp[i][j - k], dp[i + 1][j])
		return int(dp[m][n])



obj = Solution()
robot = [0,4,6]
factory = [[2,2],[6,2]]
print(obj.minimumTotalDistance(robot, factory))