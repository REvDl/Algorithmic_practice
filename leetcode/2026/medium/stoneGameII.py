from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
      n = len(piles)
      dp = [[0] * (n + 1) for _ in range(n + 1)]
      M = 1
      suff = [0] * (n + 1)
      for i in range(n -1, -1, -1):
        suff[i] = suff[i + 1] + piles[i]
      for i in range(n -1, -1, -1):
        for M in range(1, n+1):
          if (i + M * 2) >= n:
            dp[i][M] = suff[i]
          else:
            for x in range(1, 2 * M + 1):
              dp[i][M] = max(suff[i] - dp[i+x][max(x, M)], dp[i][M])
      return dp[0][1]