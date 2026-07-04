from typing import List
from collections import deque


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        def bfs(graph, start_node):
            min_dist = float("inf")
            queue = deque([start_node])
            visited = set()
            while queue:
                node = queue.popleft()
                for v, dist in graph[node]:
                    if v not in visited:
                        queue.append(v)
                        visited.add(v)
                    min_dist = min(min_dist, dist)
            return min_dist
        return bfs(graph, 1)



obj = Solution()
n = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
print(obj.minScore(n, roads))


        
