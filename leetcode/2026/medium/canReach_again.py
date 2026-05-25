from typing import List



class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        last_index = 0
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            j = max(i + minJump, last_index)
            while j <= min(i + maxJump, n - 1):
                if s[j] == "0":
                    dp[j] = True
                j += 1
            last_index = j
        return dp[n-1]

obj = Solution()
s = "011010"
minJump = 2
maxJump = 3
print(obj.canReach(s, minJump, maxJump))
