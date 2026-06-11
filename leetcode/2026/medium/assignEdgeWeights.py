from typing import List
from collections import defaultdict



class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        max_distance = [0]
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent_node, distance):
            if distance > max_distance[0]:
                max_distance[0] = distance
            for neighbor in graph[node]:
                if neighbor != parent_node:
                    dfs(neighbor, node, distance + 1)
        dfs(1, -1, 0)
        return pow(2, max_distance[0] - 1, (10**9) + 7)
