from typing import List


class Solution:
	def canPartitionGrid(self, grid: List[List[int]]) -> bool:
		rows, cols = len(grid), len(grid[0])
		rows_sum = [sum(grid[r]) for r in range(rows)]
		total_sum = sum(rows_sum)
		if total_sum % 2 != 0:
			return False
		target = total_sum // 2
		current_sum = 0
		for num in rows_sum:
			current_sum += num
			if current_sum == target:
				return True
		cols_sum = [0] * cols
		for i in range(rows):
			for j in range(cols):
				cols_sum[j] += grid[i][j]
		current_sum = 0
		for num in cols_sum:
			current_sum += num
			if current_sum == target:
				return True
		return False




obj = Solution()
arr = [[58068,1027,18371,19994,38195,17811,28277,46139],[71905,43507,3995,12186,11475,67976,61706,56109],[25332,92530,27101,93432,14666,50201,95675,17069],[71530,34478,93051,73890,75298,32212,70879,54085],[99654,9310,961,65932,38239,590,45048,85604]]
print(obj.canPartitionGrid(arr))