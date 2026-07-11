from typing import List
from collections import defaultdict, deque


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        def bfs(node, graph, n, visited):
            queue = deque([node])
            visited[node] = True
            comp_nodes = 0
            total_degree = 0
            while queue:
                val = queue.popleft()
                comp_nodes += 1
                total_degree += len(graph[val])
                for v in graph[val]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            return comp_nodes, total_degree
        res = 0
        complete_components_count = 0
        for i in range(n):
            if not visited[i]:
                Vc, total_degree = bfs(i, graph, n, visited)
                Ec = total_degree // 2
                if Ec == ((Vc * (Vc - 1)) // 2):
                    res += 1
        return res




obj = Solution()
n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]
print(obj.countCompleteComponents(n, edges))
