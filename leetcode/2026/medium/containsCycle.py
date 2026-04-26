from typing import List


class Solution:
	def containsCycle(self, grid: List[List[str]]) -> bool:
		n,m = len(grid), len(grid[0])
		directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		visited = [[False for _ in range(m)] for _ in range(n)]
		def dfs(r:int, c:int, prev_r:int, prev_c:int):
			visited[r][c] = True
			for dr, dc in directions:
				nr, nc = r + dr, c + dc
				if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == grid[r][c]:
					if visited[nr][nc]:
						if (nr != prev_r or nc != prev_c):
							return True
					else:
						if dfs(nr, nc, r, c):
							return True
			return False
		for i in range(n):
			for j in range(m):
				if not visited[i][j]:
					if dfs(i, j, -1, -1):
						return True
		return False


obj = Solution()
grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
print(obj.containsCycle(grid))