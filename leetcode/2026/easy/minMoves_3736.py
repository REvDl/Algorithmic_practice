from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        return sum([max_num - num for num in nums])



obj = Solution()
nums = [2,1,3]
print(obj.minMoves(nums))
