from sortedcontainers import SortedList
import heapq
from collections import defaultdict


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        n = len(arrival)
        free_servers = SortedList([i for i in range(k)])
        busy_servers = []
        heapq.heapify(busy_servers)
        ans = defaultdict(int)
        for i in range(n):
            while busy_servers and busy_servers[0][0] <= arrival[i]:
                _, idx = heapq.heappop(busy_servers)
                free_servers.add(idx)
            if free_servers:
                idx = free_servers.bisect_left(i % k)
                if idx == len(free_servers):
                    idx = 0
                server_idx = free_servers[idx]
                ans[server_idx] += 1
                heapq.heappush(busy_servers, (arrival[i] + load[i], server_idx))
                free_servers.pop(idx)
            else:
                continue
        max_val = max(ans.values())
        return [k for k, v in ans.items() if v == max_val]



obj = Solution()
k = 3
arrival = [1,2,3]
load = [10,12,11]
print(obj.busiestServers(k, arrival, load))
