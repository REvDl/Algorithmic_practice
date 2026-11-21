from typing import List
from functools import cache



class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        new_parent = [0] * n
        for x in range(1, n):
            curr_node = parent[x]
            while curr_node != -1:
                if s[curr_node] == s[x]:
                    new_parent[x] = curr_node
                    break
                else:
                    new_parent[x] = parent[x]
                curr_node = parent[curr_node]

        answer = [1] * n
        children = [[] for _ in range(n)]
        for i in range(n):
            p = new_parent[i]
            if p != i:
                children[p].append(i)
        @cache
        def dfs(u):
            res = 0
            for v in children[u]:
                child_res = dfs(v)
                res += child_res
            return res + 1
        for num in new_parent:
            answer[num] = dfs(num)
        return answer


obj = Solution()
parent =[-1,0,0,1,1,1]
s = "abaabc"
print(obj.findSubtreeSizes(parent, s))
