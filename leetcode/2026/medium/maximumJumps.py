from typing import List


class Solution:
	def maximumJumps(self, nums: List[int], target: int) -> int:
		n = len(nums)
		dp = [float("-inf") for _ in range(n)]
		dp[0] = 0
		for i in range(1, n):
			for j in range(i):
				if j < n and -target <= nums[j] - nums[i] <= target:
					dp[i] = max(dp[i], dp[j] + 1)
		max_step = dp[n-1]
		return max_step if max_step > 0 else -1





obj = Solution()
nums = [1,3,6,4,1,2]
target = 0
print(obj.maximumJumps(nums, target))

