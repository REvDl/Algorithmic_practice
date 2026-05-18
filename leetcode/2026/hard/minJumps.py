from typing import List
from collections import deque, defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr) - 1
        steps_map = defaultdict(list)
        for index, val in enumerate(arr):
            steps_map[val].append(index)
        def bfs(node, graph):
            queue = deque([(0, 0)])
            curr = node
            while queue:
                next_steps = []
                index, steps = queue.popleft()
                if index == n:
                    return steps
                if index + 1 <= n:
                    next_steps.append(index + 1)
                if index - 1 >= 0:
                    next_steps.append(index - 1)
                for i in steps_map[arr[index]]:
                    if i != index:
                        next_steps.append(i)
                for neigh in next_steps:
                    queue.append((neigh, steps + 1))

        return bfs(arr, 0)
 

obj = Solution()
arr = [100,-23,-23,404,100,23,23,23,3,404]
print(obj.minJumps(arr))
