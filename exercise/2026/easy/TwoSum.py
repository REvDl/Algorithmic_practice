class Solution(object):
	def twoSum(self, nums: list[int], target:int):
		result = dict()
		for i, num in enumerate(nums):
			remainder = target - num
			if remainder in result:
				return [result[remainder], i]
			else:
				result[num] = i
		return None