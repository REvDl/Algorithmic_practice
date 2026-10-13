from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares_num = sorted(x * x for x in nums)
        mid = len(nums) // 2
        return sum(squares_num[mid:]) - sum(squares_num[:mid]) 




obj = Solution()
nums = [1,2,3]
print(obj.maxAlternatingSum(nums))
