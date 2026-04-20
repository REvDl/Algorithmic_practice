from typing import List


class Solution:
	def maxDistance(self, colors: List[int]) -> int:
		result = 0
		n = len(colors)
		for i in range(n -1, -1, -1):
			if colors[i] != colors[0]:
				result = max(result, i)
		for j in range(n -1):
			if colors[j] != colors[-1]:
				result = max(result, (abs(j - (n - 1))))
		return result

	def maxDistance_v2(self, colors: List[int]) -> int:
		max_diss = 0
		for i in range(len(colors)-1, -1, -1):
			if colors[i] != colors[0]:
				max_diss = max(max_diss, i)
				break
		for j in range(len(colors)-1):
			if colors[j] != colors[-1]:
				max_diss = max(max_diss, abs(j - (len(colors) - 1)))
				break
		return max_diss

obj = Solution()
colors = [4,4,4,11,4,4,11,4,4,4,4,4]
print(obj.maxDistance(colors))
print(obj.maxDistance_v2(colors))


