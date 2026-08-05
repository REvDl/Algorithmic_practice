from typing import List
from collections import deque, defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        infected = {k}
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
        queue = deque([k])
        visited = [False] * n
        visited[k] = True
        while queue:
            a = queue.popleft()
            for b in graph[a]:
                if not visited[b]:
                    visited[b] = True
                    infected.add(b)
                    queue.append(b)
        for a, b in invocations:
            if b in infected and a not in infected:
                return list(range(n))
        return [i for i in range(n) if i not in infected]


obj = Solution()
n = 3
k = 2
invocations = [[1,2],[0,1],[2,0]]
print(obj.remainingMethods(n, k, invocations))
