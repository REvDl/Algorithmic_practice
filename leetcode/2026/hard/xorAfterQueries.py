from typing import List
from math import sqrt


class Solution:
	def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
		INF = 10 ** 9 + 7
		SQRT = int(sqrt(len(nums)))
		result = 0
		steps_update = [[] for _ in range(SQRT)]
		for query in queries:
			l, r, k, v = query[0], query[1], query[2], query[3]
			if k >= SQRT:
				for i in range(l, r + 1, k):
					nums[i] = (nums[i]* v) % INF
			else:
				steps_update[k].append((l, r, v))

		dif = [1] * (len(nums) + SQRT + 1)
		for k in range(1, SQRT):
			if not steps_update[k]:
				continue
			for i in range(len(dif)):
				dif[i] = 1
			for l, r, v in steps_update[k]:
				dif[l] = (dif[l] * v) % INF
				steps = (r - l) // k
				R = l + (steps + 1) * k
				if R < len(dif):
					dif[R] = (dif[R] * pow(v, INF - 2, INF)) % INF
			for i in range(k, len(nums)):
				dif[i] = (dif[i] * dif[i - k]) % INF
			for i in range(len(nums)):
				nums[i] = (nums[i] * dif[i]) % INF

		ans = 0
		for x in nums:
			ans ^= x
		return ans


obj = Solution()
nums = [885,987,895,774,247,820,747,826,377]
queries = [[1,7,7,9],[4,7,2,15]]
print(obj.xorAfterQueries(nums, queries))