from collections import Counter
from typing import List


class Solution:
	def isGood_bad_version(self, nums: List[int]) -> bool:
		base_n = max(nums)
		counter_nums = Counter(nums)
		if counter_nums.get(base_n) == 2:
			for i in range(len(nums)):
				if nums[i] != base_n and counter_nums.get(nums[i]) >= 2:
					return False
			return True
		return False

	def isGood_v2(self, nums: List[int]) -> bool:
		base_n = max(nums)
		base = []
		for i in range(1, base_n):
			base.append(i)
		base[len(base):] = [base_n, base_n]
		nums.sort()
		return base == nums

	def isGood_v3(self, nums: List[int]) -> bool:
		nums.sort()
		base_n = nums[-1]
		base = list(range(1, base_n)) + [base_n, base_n]
		return base == nums


obj = Solution()
nums = [1, 3, 3, 2]
print(obj.isGood_v3(nums))