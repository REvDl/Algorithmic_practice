from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist = [[-1] * cols for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        max_heap = [(-dist[0][0], 0, 0)]
        max_safeness = [[-1] * cols for _ in range(rows)]
        max_safeness[0][0] = dist[0][0]
        while max_heap:
            safe, r, c = heapq.heappop(max_heap)
            safe = -safe
            if r == rows -1 and c == cols - 1:
                return safe
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    next_safe = min(safe, dist[nr][nc])
                    if next_safe > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = next_safe
                        heapq.heappush(max_heap, (-next_safe, nr, nc))
        return 0
