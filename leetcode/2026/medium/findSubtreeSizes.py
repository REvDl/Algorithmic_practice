from re import sub
from typing import List
from functools import cache
from collections import defaultdict
import sys


sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        new_parent = [0] * n
        children = [[] for _ in range(n)]
        for i in range(n):
            p = parent[i]
            if p != -1:
                children[p].append(i)
        letters = {}
        def subtree(u):
            prev = letters.get(s[u], -1)
            if prev != -1:
                new_parent[u] = letters[s[u]]
            else:
                new_parent[u] = parent[u]
            letters[s[u]] = u
            for v in children[u]:
                subtree(v)
            letters[s[u]] = prev
        subtree(0)
        answer = [1] * n
        children = [[] for _ in range(n)]
        for i in range(n):
            p = new_parent[i]
            if p != -1:
                children[p].append(i)
        @cache
        def dfs(u):
            res = 0
            for v in children[u]:
                child_res = dfs(v)
                res += child_res
            return res + 1
        for i in range(n):
            answer[i] = dfs(i)
        return answer


obj = Solution()
parent =[-1,0,0,1,1,1]
s = "abaabc"
print(obj.findSubtreeSizes(parent, s))
