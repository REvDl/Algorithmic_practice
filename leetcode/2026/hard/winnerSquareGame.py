

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j**2 <= i:
                if not dp[i - j*j]:
                    dp[i] = True
                    break
                else:
                    dp[i] = False
                j += 1
        return dp[n]

obj = Solution()
n = 1
print(obj.winnerSquareGame(n))
