from collections import defaultdict

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        MOD = 10**9+7
        visited = defaultdict(int)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            dp[i] = (2 * dp[i - 1]) % MOD
            if s[i-1] in visited:
                dp[i] = (2 * dp[i - 1] - dp[visited[s[i-1]]-1] + MOD) % MOD
            visited[s[i-1]] = i
        return (dp[n] - 1) % MOD



obj = Solution()
tests = {"aaa":3, "aba":6, "baaa":7}
for test in tests.items():
    print(obj.distinctSubseqII(test[0]), test[1])
