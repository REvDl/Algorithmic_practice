from typing import List


class Solution:
	def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
		INF = 10**9 + 7
		result = 0
		for query in queries:
			li, ri, ki, vi = query[0], query[1], query[2], query[3]
			idx = li
			while idx <= ri:
				nums[idx] = (nums[idx] * vi) % INF
				idx += ki
		for num in nums:
			result ^= num
		return result



obj = Solution()
nums = [1,1,1]
queries = [[0,2,1,4]]
print(obj.xorAfterQueries(nums, queries))