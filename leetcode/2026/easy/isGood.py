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




obj = Solution()
nums = [1, 3, 3, 2]
print(obj.isGood_bad_version(nums))