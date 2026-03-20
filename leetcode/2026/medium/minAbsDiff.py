from typing import List


class Solution:
	def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
		rows, cols = len(grid), len(grid[0])
		ans = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]
		for i in range(rows - k + 1):
			for j in range(cols - k + 1):
				elements = set()
				for r in range(i, i + k):
					for c in range(j, j + k):
						elements.add(grid[r][c])
				elements = sorted(list(elements))
				if len(elements) < 2:
					ans[i][j] = 0
					continue
				diff = float("inf")
				for element in range(1, len(elements)):
					current = abs(elements[element] - elements[element - 1])
					if current < diff:
						diff = current
				ans[i][j] = diff
		return ans




obj = Solution()
grid = [[1,-2,3],[2,3,5]]
print(obj.minAbsDiff(grid, 2))