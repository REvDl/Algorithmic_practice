from typing import List


class Solution:
	def separateDigits(self, nums: List[int]) -> List[int]:
		separate_nums = []
		for num in nums:
			separate = list(str(num))
			for num_sep in separate:
				separate_nums.append(int(num_sep))
		return separate_nums




obj = Solution()
nums = [10, 12, 1, 5, 33]
print(obj.separateDigits(nums))