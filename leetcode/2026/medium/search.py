from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left, right = 0, len(nums) - 1
		while left <= right:
			mid = (left + right) // 2
			if nums[mid] == target:
				return mid
			left_val, right_val, mid_val = nums[left], nums[right], nums[mid]
			if left_val <= mid_val:
				if left_val <= target <= mid_val:
					right = mid - 1
				else:
					left = mid + 1
			else:
				if mid_val <= target <= right_val:
					left = mid + 1
				else:
					right = mid - 1
		return -1




# def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
# 	left, right = start, start
# 	n = len(nums)
# 	while left >= 0 or right < n:
# 		if nums[left] == target:
# 			return left - start
# 		if nums[right] == target:
# 			return right - start
# 		left -= 1
# 		left += 1


obj = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(obj.search(nums, target))