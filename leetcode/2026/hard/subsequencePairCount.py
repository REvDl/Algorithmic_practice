from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 201 for _ in range(201)]
        dp[0][0] = 1
        MOD = 10**9+7
        for num in nums:
            next_dp = [row[:] for row in dp]
            for g1 in range(201):
                for g2 in range(201):
                    count = dp[g1][g2]
                    if count == 0:
                        continue
                    new_g1 = num if g1 == 0 else gcd(g1, num)
                    next_dp[new_g1][g2] = (next_dp[new_g1][g2] + count) % MOD
                    new_g2 = num if g2 == 0 else gcd(g2, num)
                    next_dp[g1][new_g2] = (next_dp[g1][new_g2] + count) % MOD
            dp = next_dp
        ans = 0
        for num in range(1, 201):
            ans = (ans + dp[num][num]) % MOD
        return ans
obj = Solution()
nums = [1, 2, 3, 4]
print(obj.subsequencePairCount(nums))
