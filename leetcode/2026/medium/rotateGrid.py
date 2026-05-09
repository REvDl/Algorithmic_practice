from typing import List


class Solution:
	def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
		n, m = len(grid), len(grid[0])
		layers = min(n, m) // 2
		for layer in range(layers):
			up, down, left, right = layer, n - 1 - layer, layer, m - 1 - layer
			w, h = right - left + 1, down - up + 1
			L = w * 2 + h * 2 - 4
			current_k = k % L
			coords_grid = []
			for j in range(left, right):     coords_grid.append((up, j))
			for i in range(up, down):       coords_grid.append((i, right))
			for j in range(right, left, -1): coords_grid.append((down, j))
			for i in range(down, up, -1):    coords_grid.append((i, left))
			flat = [grid[i][j] for i, j in coords_grid]
			shift = flat[current_k:] + flat[:current_k]

			for (x, y), val in zip(coords_grid, shift):
				grid[x][y] = val
		return grid




obj = Solution()
grid = [[40,10],[30,20]]
k = 1
print(obj.rotateGrid(grid, k))
