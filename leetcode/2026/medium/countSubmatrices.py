from typing import List


class Solution:
	def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
		rows, cols = len(grid), len(grid[0])
		count = 0
		for i in range(rows):
			for j in range(cols):
				if i > 0: grid[i][j] += grid[i - 1][j]
				if j > 0: grid[i][j] += grid[i][j - 1]
				if i > 0 and j > 0: grid[i][j] -= grid[i-1][j-1]
				if grid[i][j] <= k:
					count += 1
				else:
					break
		return count


obj = Solution()
arr = [[7,2,9],[1,5,0],[2,6,6]]
print(obj.countSubmatrices(arr, 20))

