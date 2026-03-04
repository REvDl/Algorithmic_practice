from typing import List


class Solution:
	def rob(self, nums: List[int]) -> int:
		if not nums:
			return 0
		prev1 = 0
		prev2 = 0
		for num in nums:
			tmp = prev1
			prev1 = max(prev2 + num, prev1)
			prev2 = tmp
		return prev1

obj = Solution()
print(obj.rob([3,1,1,3]))
