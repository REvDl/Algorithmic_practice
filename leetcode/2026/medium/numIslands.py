from typing import List
from collections import deque



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c)])
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(0,1), (0,-1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == '1':
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    ans += 1
                    visited.add((r, c))
                    bfs(r,c)
        return ans



obj = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(obj.numIslands(grid))

