from typing import List


class Solution:
	def maxRotateFunction(self, nums: List[int]) -> int:
		n = len(nums)
		total_sum = 0
		F = 0
		for i in range(n):
			total_sum += nums[i]
			F += i * nums[i]
		max_rotate = F
		for i in range(1, n):
			last_idx = n - i
			F += total_sum - (nums[last_idx] * n)
			max_rotate = max(max_rotate, F)
		return max_rotate

obj = Solution()
nums = [1,2,3,4,5,6,7,8,9,10]
print(obj.maxRotateFunction(nums))