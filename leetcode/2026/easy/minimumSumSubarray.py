from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        for left in range(n):
            for k in range(l, r + 1):
                if (left + k) <= n:
                    curr_sum = prefix_sum[left + k] - prefix_sum[left]
                    if curr_sum > 0:
                        min_sum = min(min_sum, curr_sum)
        return -1 if min_sum == float('inf') else min_sum



obj = Solution()
nums = [3, -2, 1, 4]
l = 2
r = 3
print(obj.minimumSumSubarray(nums, l, r))
