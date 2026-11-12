from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left_inc = 0
        left_dec = 0
        max_inc = 1
        max_dec = 1

        for right in range(1, len(nums)):
            if nums[right - 1] >= nums[right]:
                left_inc = right
            max_inc = max(max_inc, right - left_inc + 1)

            if nums[right - 1] <= nums[right]:
                left_dec = right
            max_dec = max(max_dec, right - left_dec + 1)
        return max(max_inc, max_dec)


obj = Solution()
nums = [[1,4,3,3,2], [3,3,3,3], [3,2,1], [1,2]]
for num in nums:
    print(obj.longestMonotonicSubarray(num))
