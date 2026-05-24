



class Solution:
    def canReach_v1(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            j = i + minJump
            while j <= min(i + maxJump, n - 1):
                if s[j] == "0":
                    dp[j] = True
                j += 1
        return dp[n-1]

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        farthest = 0
        for i in range(n):
            if not dp[i]:
                continue
            j = max(i + minJump, farthest)
            while j <= min(i + maxJump, n - 1):
                if s[j] == "0":
                    dp[j] = True
                j += 1
            farthest = j
        return dp[n-1]   



obj = Solution()
s = "011010"
minJump = 2
maxJump = 3
print(obj.canReach(s, minJump, maxJump))
