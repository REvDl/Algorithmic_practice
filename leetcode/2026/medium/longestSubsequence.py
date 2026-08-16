from typing import List
from functools import reduce


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if nums.count(0) == n:
            return 0
        res = 0
        for num in nums: res ^= num
        if res != 0:
            return n
        return n - 1






obj = Solution()
nums = [2,3,4]
print(obj.longestSubsequence(nums))
