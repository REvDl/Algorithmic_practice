from typing import List



class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group_id = [0] * n
        id_count = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                id_count += 1
            group_id[i] = id_count                
        ans = []
        for ui, vi in queries:
            ans.append(group_id[ui] == group_id[vi])
        return ans

obj = Solution()
n = 4
nums = [2,5,6,8]
maxDiff = 2
queries = [[0,1],[0,2],[1,3],[2,3]]
print(obj.pathExistenceQueries(n, nums, maxDiff, queries))
