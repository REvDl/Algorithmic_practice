


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        K = r - l + 1
        MOD = 10**9 + 7
        dp = [[[0] * K for _ in range(2)] for _ in range(n + 1)]
        for i in range(K):
            dp[1][1][i] = 1
            dp[1][0][i] = 1

        for i in range(2, n + 1):
            prefix_0 = [0] * (K + 1)
            prefix_1 = [0] * (K + 1)
            for idx in range(K):
                prefix_0[idx + 1] = (prefix_0[idx] + dp[i-1][0][idx]) % MOD
                prefix_1[idx + 1] = (prefix_1[idx] + dp[i-1][1][idx]) % MOD
            for x in range(K):
                dp[i][0][x] = (prefix_1[K] - prefix_1[x + 1] + MOD) % MOD
                dp[i][1][x] = prefix_0[x] 
        return sum(dp[n][0] + dp[n][1]) % MOD


class Solution_2:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        K = r - l + 1
        MOD = 10**9 + 7
        dp0 = [1] * K
        dp1 = [1] * K
        for _ in range(2, n + 1):
            next_dp0 = [0] * K
            next_dp1 = [0] * K
            pref0 = 0
            for x in range(K):
                next_dp1[x] = pref0
                pref0 = (pref0 + dp0[x]) % MOD
            suff1 = 0
            for x in range(K - 1, -1, -1):
                next_dp0[x] = suff1
                suff1 = (suff1 + dp1[x]) % MOD
            dp0 = next_dp0
            dp1 = next_dp1          
        return (sum(dp0) + sum(dp1)) % MOD
obj = Solution()
n = 3
l = 1
r = 3
print(obj.zigZagArrays(n, l, r))
