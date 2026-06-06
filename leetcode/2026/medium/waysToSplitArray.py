from typing import List



class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        valid_splits = 0
        left_sum = 0
        for i in range(n - 1):
            left_sum += nums[i]
            total_sum -= nums[i]
            if left_sum >= total_sum:
                valid_splits += 1
        return valid_splits



obj = Solution()
nums = [10,4,-8,7]
print(obj.waysToSplitArray(nums))
