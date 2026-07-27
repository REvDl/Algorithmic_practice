from typing import List




class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] - 1) * (nums[-1] - 1)



obj = Solution()
nums = [3,4,5,2]
print(obj.maxProduct(nums))
