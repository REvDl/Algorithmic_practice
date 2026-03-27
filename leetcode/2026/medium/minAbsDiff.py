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
				elements = sorted(elements)
				if len(elements) < 2:
					diff = 0
					continue
				diff = float("inf")
				for element in range(len(elements) - 1):
					res = abs(elements[element] - elements[element + 1])
					if res < diff:
						diff = res
				ans[i][j] = diff
		return ans


obj = Solution()
grid = [[3,-1]]
print(obj.minAbsDiff(grid, 1))