import time
from functools import wraps
from typing import List



def timer(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		result = start - time.time()
		return result
	return wrapper






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


	def only_min(self, nums: List[int]) -> int:
		return min(nums)


obj = Solution()
part_left = [6] * 2000
target = [-10]
part_right = [5] * 2000

test_case = part_left + target + part_right
print(obj.findMin(test_case))
print(timer(obj.findMin)(test_case))
print(timer(obj.only_min)(test_case))
