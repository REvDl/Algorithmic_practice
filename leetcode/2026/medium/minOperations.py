from typing import List


class Solution:
	def minOperations(self, grid: List[List[int]], x: int) -> int:
		arr_grid = [item for arr in grid for item in arr]
		arr_grid.sort()
		steps = 0
		median = arr_grid[len(arr_grid) // 2]
		for item in arr_grid:
			step = abs(item - median)
			if step % x != 0:
				return -1
			steps += step // x
		return steps


	def minOperations_v2(self, grid: List[List[int]], x: int) -> int:
		arr_grid = [item for arr in grid for item in arr]
		for item in arr_grid:
			if (arr_grid[0] - item) % x != 0:
				return -1
		arr_grid.sort()
		median = arr_grid[len(arr_grid) // 2]
		step = 0
		for item in arr_grid:
			step += abs(item - median) // x
		return step




obj = Solution()
grid = [[2,4],[6,8]]
x = 2
print(obj.minOperations(grid, x))