from typing import List
import math
from collections import Counter


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [0] * k
        dp = [0] * k
        for num in nums:
            next_dp = [0] * k
            for j in range(k):
                new_rem = (j * num) % k
                next_dp[new_rem] += dp[j]
            next_dp[num % k] += 1
            for r in range(k):
                res[r] += next_dp[r]
            dp = next_dp
        return res

obj = Solution()
nums = [1,2,3,4,5]
k = 3
print(obj.resultArray(nums, k))
