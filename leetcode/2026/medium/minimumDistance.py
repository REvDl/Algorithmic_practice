from collections import defaultdict
from typing import List


class Solution:
	def minimumDistance(self, nums: List[int]) -> int:
		result = []
		positions = defaultdict(list)
		for i, val in enumerate(nums):
			positions[val].append(i)

		for element in positions.values():
			if len(element) >= 3:
				for num in range(len(element) - 2):
					i, j, k = element[num], element[num + 1], element[num + 2]
					dis = 2 * (k - i)
					result.append(dis)
		return min(result) if result else -1




obj = Solution()
nums = [5,3,5,5,5]
print(obj.minimumDistance(nums))


nums = [1,2,1,1,3]
print(obj.minimumDistance(nums))


nums = [1,1,2,3,2,1,2]
print(obj.minimumDistance(nums))

