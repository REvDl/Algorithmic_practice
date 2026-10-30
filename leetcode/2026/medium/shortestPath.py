from typing import List
import heapq
from collections import defaultdict




class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        distances = {i: {} for i in range(n)}
        distances[0][1] = 0
        pq = [(0, 0, 1)]
        while pq:
            current_dist, u, run = heapq.heappop(pq)
            if current_dist > distances[u].get(run, float("inf")):
                continue

            for v, weight in graph[u]:
                distance = current_dist + weight
                if labels[u] == labels[v]:
                    new_run = run + 1
                    if new_run > k:
                        continue
                else:
                    new_run = 1
                if distance < distances[v].get(new_run, float("inf")):
                    distances[v][new_run] = distance
                    heapq.heappush(pq, (distance, v, new_run))
    
        return -1 if not distances[n-1] else min(distances[n-1].values())

obj = Solution()
n = 3
edges = [[0,1,1],[1,2,1],[0,2,3]]
labels = "aab"
k = 1
print(obj.shortestPath(n, edges, labels, k))
