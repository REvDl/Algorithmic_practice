from typing import List
import heaqp


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_health = [[-1] * n for _ in range(m)]
        start_health = health - 1 if grid[0][0] == 1 else health
        if start_health < 1:
            return False
        max_health[0][0] = start_health
        max_heap = [(-start_health, 0, 0)]
        while max_heap:
            hp, r, c = heapq.heappop(max_heap)
            hp = -hp
            if r == m - 1 and c == n - 1:
                return hp >= 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n:
                    next_hp = hp - grid[nr][nc]
                    if next_hp > max_health[nr][nc]:
                        max_health[nr][nc] = next_hp
                        heapq.heappush(max_heap, (-next_hp, nr, nc))
        return False
