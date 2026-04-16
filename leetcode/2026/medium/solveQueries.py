from typing import List
from collections import  defaultdict
from bisect import bisect_left



class Solution:
	def solveQueries_v1(self, nums: List[int], queries: List[int]) -> List[int]:
		idxs = defaultdict(list)
		result_idx = []
		n = len(nums)
		for i, val in enumerate(nums):
			idxs[val].append(i)

		for query in queries:
			val = nums[query]
			target_idx = idxs[val]
			diss = float("inf")
			for idx in target_idx:
				if idx == query:
					continue
				d = abs(query - idx)
				diss = min(diss, d, n - d)
			if diss == float("inf"):
				result_idx.append(-1)
			else:
				result_idx.append(diss)
		return result_idx

	def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
		idxs, n = defaultdict(list), len(nums)
		result_idx = []
		for i, val in enumerate(nums):
			idxs[val].append(i)



		for query in queries:
			diss = float("inf")
			val = nums[query]
			target_idx = idxs[val]
			i = bisect_left(target_idx, query)
			d = abs(query - target_idx[(i-1) % len(target_idx)])
			b = abs(query - target_idx[(i+1) % len(target_idx)])
			diss = min(d, n - d, b, n - b)
			if diss == 0:
				result_idx.append(-1)
			else:
				result_idx.append(diss)
		return result_idx







obj = Solution()
nums = [1, 3, 1, 4, 1, 3, 2]
queries = [0, 3, 5]
print(obj.solveQueries(nums, queries))
# Expected Output: [2,-1,3]
