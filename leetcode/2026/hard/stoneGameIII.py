from typing import List



class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)
        stoneValue_padded = stoneValue + [0, 0, 0]
        for i in range(n - 1, -1, -1):
            two_stones = stoneValue_padded[i] + stoneValue_padded[i + 1]
            three_stones = two_stones + stoneValue_padded[i + 2]
            dp[i] = max(stoneValue_padded[i] - dp[i + 1], two_stones - dp[i + 2], three_stones - dp[i + 3])
        winner = "Tie"
        if dp[0] > 0:
            winner = "Alice"
        elif dp[0] < 0:
            winner = "Bob"
        return winner



obj = Solution()
stoneValue = [1,2,3,7]
print(obj.stoneGameIII(stoneValue))

