from typing import List


class Solution:
	def minMoves(self, nums: List[int], limit: int) -> int:
		prefix_sum = [0] * ((limit * 2) + 2)
		n = len(nums)
		for i in range(n // 2):
			A = nums[i]
			B = nums[n - 1 - i]
			min_i = min(A, B) + 1
			max_i = max(A, B) + limit
			sum_num = A + B
			prefix_sum[min_i] -= 1
			prefix_sum[max_i + 1] += 1
			prefix_sum[sum_num] -= 1
			prefix_sum[sum_num + 1] += 1
		result = n
		moves = n
		for i in range(2, 2 * limit + 1):
			moves += prefix_sum[i]
			result = min(result, moves)
		return result




obj = Solution()
nums = [1,2,4,3]
limit = 4
print(obj.minMoves(nums, limit))