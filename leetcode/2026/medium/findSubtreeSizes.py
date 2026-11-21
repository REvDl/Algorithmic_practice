from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        answer = [1] * n
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
        for i in range(n):
            curr_node = i
            while new_parent[curr_node] != curr_node:
                curr_node = new_parent[curr_node]
                answer[curr_node] += 1
        return answer

obj = Solution()
parent =[-1,0,0,1,1,1]
s = "abaabc"
print(obj.findSubtreeSizes(parent, s))
