from typing import List


class Solution:
	def findMin(self, nums: List[int]) -> int:
		left, right = 0, len(nums) - 1
		while left < right:
			mid = (left + right) // 2
			num = nums[mid]
			if num > nums[right]:
				left = mid + 1
			else:
				right = mid
		return nums[right]





obj = Solution()
nums = [4,6,7,10,17,1, 11, 0]
print(obj.findMin(nums))