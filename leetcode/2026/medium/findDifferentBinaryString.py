from typing import List


class Solution:
	def findDifferentBinaryString(self, nums: List[str]) -> str:
		n = len(nums)
		result_string = ""
		for i in range(n):
			if nums[i][i] == "0":
				result_string += "1"
			if nums[i][i] == "1":
				result_string += "0"
		return result_string



nums = ["111", "011", "001"]
obj = Solution()
print(obj.findDifferentBinaryString(nums))