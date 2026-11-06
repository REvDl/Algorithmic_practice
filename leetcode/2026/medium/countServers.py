from typing import List
from collections import Counter


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))
        logs.sort(key = lambda x: x[1])
        arr = [0] * len(queries)
        count = Counter()
        active_servers = 0
        left, right = 0, 0
        for server_time, original_index in sorted_queries:
            while right < len(logs) and logs[right][1] <= server_time:
                count[logs[right][0]] += 1
                if count[logs[right][0]] == 1:
                    active_servers += 1
                right += 1
            while left < len(logs) and logs[left][1] < (server_time - x):
                count[logs[left][0]] -= 1
                if count[logs[left][0]] == 0:
                    active_servers -= 1
                left += 1
            arr[original_index] = n - active_servers
        return arr


obj = Solution()
n = 3
logs = [[1,3],[2,6],[1,5]]
x = 5
queries = [10,11]
print(obj.countServers(n, logs, x, queries))
