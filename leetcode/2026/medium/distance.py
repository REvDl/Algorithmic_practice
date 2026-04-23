from typing import List
from collections import defaultdict

class Solution:
	def distance(self, nums: List[int]) -> List[int]:
		groups = defaultdict(list)
		n = len(nums)
		arr = [0] * n
		for i, val in enumerate(nums):
			groups[val].append(i)
		for val, pos in groups.items():
			total_sum, current_prefix_sum = sum(pos), 0
			for i in range(len(pos)):
				count_right = len(pos) - 1 - i
				target_index = pos[i]

				index_sum_left = (i * target_index) - current_prefix_sum
				index_sum_right = (total_sum - current_prefix_sum - target_index) - (count_right * target_index)

				arr[target_index] = index_sum_left + index_sum_right
				current_prefix_sum += target_index
		return arr




obj = Solution()
nums = [1,3,1,1,2]
#expected [5,0,3,4,0]
print(obj.distance(nums))