from typing import List


class Solution:
	def maxValue_wrong_version(self, nums: List[int]) -> List[int]:
		result = []
		n = len(nums)
		prefix_max, sufix_min= [0] * n, [0] * n
		prefix_max[0] = nums[0]
		for i in range(1, n):
			prefix_max[i] = max(prefix_max[i - 1], nums[i])


		sufix_min[n - 1] =  n - 1
		for i in range(n -2, -1, -1):
			if prefix_max[i] <= prefix_max[sufix_min[i + 1]]:
				sufix_min[i] = i
			else:
				sufix_min[i] = sufix_min[i + 1]


		for i in range(n):
			if nums[i] > nums[sufix_min[i]]:
				result.append(prefix_max[sufix_min[i]])
			else:
				result.append(prefix_max[i])
		return result


	def maxValue(self, nums: List[int]) -> List[int]:
		n = len(nums)
		ans = [0] * n
		stack = []
		for i in range(n):
			number = nums[i]
			current_max, current_min, index = number, number, i
			while stack and number < stack[-1][1]:
				min_num, max_num, index = stack.pop()
				current_max = max(max_num, current_max)
				current_min = min(min_num, current_min)
			stack.append([current_min, current_max, index])
		for i in range(len(stack)):
			if i + 1 < len(stack):
				two_step = stack[i + 1][2]
			else:
				two_step = n
			for j in range(stack[i][2], two_step):
				ans[j] = stack[i][1]
		return ans




obj = Solution()
nums = [30,21,5,35,24]
print(obj.maxValue(nums))