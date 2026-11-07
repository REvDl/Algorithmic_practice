import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n, m = len(servers), len(tasks)
        ans = [0] * m
        curr_time = 0
        free_server = [(weight, idx) for idx, weight in enumerate(servers)]
        heapq.heapify(free_server)
        busy_server = []
        for j in range(m):
            curr_time = max(curr_time, j)
            while busy_server and busy_server[0][0] <= curr_time:
                _, weight, idx = heapq.heappop(busy_server)
                heapq.heappush(free_server, (weight, idx))
            if free_server:
                weight, idx = heapq.heappop(free_server)
                ans[j] = idx
                heapq.heappush(busy_server, (tasks[j] + curr_time, weight, idx))
            else:
                curr_time = busy_server[0][0]
                while busy_server and busy_server[0][0] <= curr_time:
                    _, weight, idx = heapq.heappop(busy_server)
                    heapq.heappush(free_server, (weight, idx))
                weight, idx = heapq.heappop(free_server)
                ans[j] = idx
                heapq.heappush(busy_server, (tasks[j] + curr_time, weight, idx))
        return ans




obj = Solution()
servers = [3,3,2]
tasks = [1,2,3,2,1,2]
print(obj.assignTasks(servers, tasks))
