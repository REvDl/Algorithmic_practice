from typing import List
from collections import defaultdict


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        parents = {}
        depth = {}
        n = len(edges) + 1
        up = [[0] * 18 for _ in range(n + 1)]
        def dfs(node, parent_node, distance):
            depth[node] = distance
            parents[node] = parent_node
            for neighbor in graph[node]:
                if neighbor != parent_node:
                    dfs(neighbor, node, distance+1)
        dfs(1, 0, 0)
        for i in range(1, n + 1):
            up[i][0] = parents.get(i, 0)

        for j in range(1, 18):
            for i in range(1, n+1):
                half = up[i][j - 1]
                if half != 0:
                    up[i][j] = up[half][j - 1]
        ans = []
        for u, v in queries:
            s_u = u
            s_v = v
            if depth[u] < depth[v]:
                u, v, = v, u
            diff = depth[u] - depth[v]
            for j in range(17, -1, -1):
                jump_size = 2 ** j
                if diff >= jump_size:
                    u = up[u][j]
                    diff -= jump_size
            if u == v:
                lca = u
                L = depth[s_u] + depth[s_v] - 2 * depth[lca]
                if L == 0:
                    ans.append(0)
                    continue
                elif L > 0:
                    ans.append(pow(2, L-1, 10**9 + 7))
                    continue
            for j in range(17, -1, -1):
                if up[u][j] != up[v][j]:
                    u,v = up[u][j],up[v][j]
            lca = up[u][0]
            L = depth[s_u] + depth[s_v] - 2 * depth[lca]
            if L == 0:
                ans.append(0)
            elif L > 0:
                ans.append(pow(2, L-1, 10**9 +7))
        return ans




obj = Solution()
edges = [[1,2],[1,3],[3,4],[3,5]]
queries = [[1,4],[3,4],[2,5]]
print(obj.assignEdgeWeights(edges, queries))
