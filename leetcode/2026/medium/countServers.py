from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        m = len(queries)
        arr = []
        for i in range(m):
            servers = set()
            for server_id, time_query in logs:
                if time_query >= queries[i] - x and time_query <= queries[i]:
                    servers.add(server_id)
            arr.append(n - len(servers))
        return arr



obj = Solution()
n = 3
logs = [[1,3],[2,6],[1,5]]
x = 5
queries = [10,11]
print(obj.countServers(n, logs, x, queries))
