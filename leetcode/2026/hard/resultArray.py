from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = []
        for query in queries:
            idx, val, start, x = query
            nums[idx] = val
            dp = [0] * k
            ways = 0
            product = 1
            for i in range(start, n):
                product = (nums[i] * product) % k
                if product == x:
                    ways += 1
            ans.append(ways)
        return ans





obj = Solution()
nums = [1,2,3,4,5]
k = 3
queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]
print(obj.resultArray(nums, k, queries))

