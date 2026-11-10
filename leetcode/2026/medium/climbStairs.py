from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            for step in range(4): 
                if i - step >= 0:
                    prev_step = i - step
                    jump_cost = costs[i - 1] + (step ** 2)
                    dp[i] = min(dp[i], dp[prev_step] + jump_cost)
        return dp[n]


obj = Solution()
n = 4
costs = [5,1,6,2]
print(obj.climbStairs(n, costs))
