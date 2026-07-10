from typing import List
from collections import deque

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_num = [(val, idx) for idx, val in enumerate(nums)]
        sorted_num.sort()
        pos = [0] * n
        for idx, val in enumerate(sorted_num):
            pos[val[1]] = idx
        right = 0
        right_bound = [0] * n
        for left in range(n):
            while right < n and sorted_num[right][0] - sorted_num[left][0] <= maxDiff:
                right += 1
            right_bound[left] = right
        def get_dist(start_node, target_node, n, right_bound):
            if start_node == target_node:
                return 0
            parent = list(range(n + 1))
            def find(i):
                if parent[i] != i:
                    parent[i] = find(parent[i])
                return parent[i]
            dist = [-1] * n
            dist[start_node] = 0
            queue = deque([start_node])
            parent[start_node] = start_node + 1
            while queue:
                p = queue.popleft()
                if p == target_node:
                    return dist[p]
                next_p = find(p)
                while next_p < right_bound[p]:
                    if dist[next_p] == -1:
                        dist[next_p] = dist[p] + 1
                        if next_p == target_node:
                            return dist[next_p]
                        queue.append(next_p)
                        parent[next_p] = next_p + 1
                    next_p = find(next_p)
            return -1

        ans = []
        for u1, v1 in queries:
            if u1 == v1:
                ans.append(0)
                continue
            u2, v2 = pos[u1], pos[v1]
            if u2 > v2:
                u2, v2 = v2, u2
            ans.append(get_dist(u2, v2, n, right_bound))
        return ans

obj = Solution()
n = 5
nums = [5,3,1,9,10]
maxDiff = 3
queries = [[0,3],[2,4]]
print(obj.pathExistenceQueries(n, nums, maxDiff, queries))
