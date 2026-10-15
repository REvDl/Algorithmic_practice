from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = []
        n = len(nums)
        for i in range(1, n+1):
            for j in range(n-i+1):
                res.append(len(set(nums[j:j+i])))
        return sum([x ** 2 for x in res])



obj = Solution()
nums = [1,2,1]
print(obj.sumCounts(nums))
