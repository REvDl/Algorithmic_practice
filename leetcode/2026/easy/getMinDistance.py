from typing import List


class Solution:
	def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
		left, right = start, start
		n = len(nums)
		while left >= 0 or right < n:
			if nums[left] == target:
				return left - start
			if nums[right] == target:
				return right - start
			left -= 1
			left += 1

obj = Solution()
nums = [1]
target = 1
start = 0
print(obj.getMinDistance(nums, target, start))