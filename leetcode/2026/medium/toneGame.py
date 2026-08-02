from typing import List



class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for k in range(1, n):
            for i in range(n - k):
                j = k + i
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[j-1][j])
        return dp[0][n-1] >= 0




obj = Solution()
piles = [5,3,4,5]
print(obj.stoneGame(piles))
