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




obj = Solution()
colors = [0,1]
print(obj.maxDistance(colors))



