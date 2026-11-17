


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                curr_str = s[i:j+1]
                l = j - i + 1
                d = 1
                count_min_replaces = float('inf')
                while d < l:
                    if l % d == 0:
                        count_replaces = 0
                        for rem in range(d):
                            left = rem
                            right = l - d + rem
                            while left < right:
                                if curr_str[left] != curr_str[right]:
                                    count_replaces += 1
                                left += d
                                right -= d
                        count_min_replaces = min(count_replaces, count_min_replaces)
                    d += 1
                cost[i][j] = count_min_replaces
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i -1):
                    dp[p][i] = min(dp[p - 1][j] + cost[j][i - 1], dp[p][i])
        return dp[k][n]


obj = Solution()
s = "abcac"
k = 2
print(obj.minimumChanges(s, k))
