from typing import List


class Solution:
	def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
		matrix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
		pointer = 1
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				matrix[i][j] = pointer
				pointer = (pointer * grid[i][j]) % 12345
		pointer = 1
		for i in range(len(grid) -1, -1, -1):
			for j in range(len(grid[0]) -1, -1, -1):
				matrix[i][j] = (matrix[i][j] * pointer) % 12345
				pointer = (pointer * grid[i][j]) % 12345
		return matrix



obj = Solution()
arr = [[1,2],[3,4]]
print(obj.constructProductMatrix(arr))