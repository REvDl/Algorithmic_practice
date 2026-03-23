from typing import List


class Solution:
	def largestAltitude(self, gain: List[int]) -> int:
		prefix_sum = [0 for _ in range(len(gain) + 1)]
		prefix_sum[0] = 0
		for i in range(len(gain)):
			prefix_sum[i + 1] = prefix_sum[i] + gain[i]
		return max(prefix_sum)


obj = Solution()
arr = [-5, 1, 5, 0, -7]
print(obj.largestAltitude(arr))
