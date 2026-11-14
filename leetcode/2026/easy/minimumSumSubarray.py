from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        n = len(nums)
        for i in range(l, r + 1):
            left = 0
            curr_sum = 0
            for right in range(n):
                curr_sum += nums[right]
                if (right - left + 1) == i:
                    if curr_sum > 0:
                        min_sum = min(min_sum, curr_sum)
                    curr_sum -= nums[left]
                    left += 1
        return -1 if min_sum == float('inf') else min_sum



obj = Solution()
nums = [3, -2, 1, 4]
l = 2
r = 3
print(obj.minimumSumSubarray(nums, l, r))
