from typing import List
import statistics


class Solution:
    def _countSteps(self, nums: List[int], start: int, end: int):
        sub_elements = [nums[j] for j in range(start, end)]
        mid = statistics.median_low(sub_elements) 
        return sum(abs(num - mid) for num in sub_elements)

    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        costs = [self._countSteps(nums, i, i + x) for i in range(n - x + 1)]
        dp = [0] * (n + 1)
        for count in range(1, k + 1):
            next_dp = [float('inf')] * (n + 1)
            for i in range(count * x, n + 1):
                start = i - x
                next_dp[i] = min(next_dp[i - 1], dp[start] + costs[start])
            dp = next_dp
        return dp[n] if dp[n] != float('inf') else -1






obj = Solution()
nums = [5,-2,1,3,7,3,6,4,-1]
x = 3
k = 2
print(obj.minOperations(nums, x, k))
