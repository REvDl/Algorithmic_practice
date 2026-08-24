from typing import List



class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            one_stone = stoneValue[i]
            if n - i >= 3:
                three_stone = one_stone + stoneValue[i + 1] + stoneValue[i + 2]
                dp[i] = max(three_stone - dp[i + 3], (one_stone + stoneValue[i + 1]) - dp[i + 2], one_stone - dp[i + 1])
            elif n - i == 2:
                two_stone = one_stone + stoneValue[i + 1]
                dp[i] = max(two_stone - dp[i + 2], one_stone - dp[i + 1])
            else:
                dp[i] = one_stone
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"



obj = Solution()
stoneValue = [1,2,3,6] 
print(obj.stoneGameIII(stoneValue))
