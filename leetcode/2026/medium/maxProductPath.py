from typing import List


class Solution:
	def maxProductPath(self, grid: List[List[int]]) -> int:
		rows, cols = len(grid), len(grid[0])
		min_arr = [[0 for _ in range(cols)] for _ in range(rows)]
		max_arr = [[0 for _ in range(cols)] for _ in range(rows)]
		max_arr[0][0] = min_arr[0][0] = grid[0][0]
		for c in range(1, cols):
			min_arr[0][c] = max_arr[0][c] = min_arr[0][c-1] * grid[0][c]
		for r in range(1, rows):
			max_arr[r][0] = min_arr[r][0] = max_arr[r - 1][0] * grid[r][0]
		for i in range(1, rows):
			for j in range(1, cols):
				value_options = [
					max_arr[i-1][j] * grid[i][j],
					max_arr[i][j-1] * grid[i][j],
					min_arr[i-1][j] * grid[i][j],
					min_arr[i][j-1] * grid[i][j],
				]
				max_arr[i][j] = max(value_options)
				min_arr[i][j] = min(value_options)
		if max_arr[rows-1][cols-1] < 0:
			return -1
		return max_arr[rows-1][cols-1] % (10**9 + 7)

obj = Solution()
arr = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
print(obj.maxProductPath(arr))