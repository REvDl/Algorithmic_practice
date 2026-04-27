from typing import List


class Solution:
	def hasValidPath(self, grid: List[List[int]]) -> bool:
		n,m = len(grid), len(grid[0])
		directions = {1: [(0, -1), (0, 1)],
					  2: [(-1, 0), (1, 0)],
					  3: [(0, -1), (1, 0)],
					  4: [(0, 1), (1, 0)],
					  5: [(0, -1), (-1, 0)],
					  6: [(0, 1), (-1, 0)]
					  }
		visited = set()
		def dfs(r:int, c:int, prev_r:int, prev_c:int):
			if (r, c) in visited:
				return False
			if r == n - 1 and c == m - 1:
				return True
			visited.add((r, c))
			for dr, dc in directions[grid[r][c]]:
				nr, nc = r + dr, c + dc
				if 0 <= nr < n and 0 <= nc < m:
					if nr != prev_r or nc != prev_c:
						if (-dr, -dc) in directions[grid[nr][nc]]:
							if dfs(nr, nc, r, c):
								return True
			return False
		return dfs(0,0, -1, -1)




obj = Solution()
grid = [[2,4,3],[6,5,2]]
print(obj.hasValidPath(grid))