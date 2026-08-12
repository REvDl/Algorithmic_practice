from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        count_nums = defaultdict(int)
        max_len = 0
        for right in range(0, n):
            count_nums[nums[right]] += 1
            while count_nums[nums[right]] > k:
                count_nums[nums[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len 






obj = Solution()
nums =[1,2,1,2,1,2,1,2]
k = 1
print(obj.maxSubarrayLength(nums, k))
