from typing import List


class Solution:
	def findMin(self, nums: List[int]) -> int:
		left, right = 0, len(nums) - 1
		while left < right:
			mid = (left + right) // 2
			if nums[mid] > nums[right]:
				left = mid + 1
			elif nums[mid] == nums[right]:
				right -= 1
			else:
				right = mid
		return nums[left]





obj = Solution()
part_left = [6] * 2000
target = [-10]
part_right = [5] * 2000

test_case = part_left + target + part_right
print(obj.findMin(test_case))
