


class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        if s.count('0') == n or s.count('1') == n:
            return 0
        ans = 0
        for i in range(0, n + 1, 2):
            sub = s[i:i + 2]
            if '1' in sub and '0' in sub:
                ans += min(sub.count('0'), sub.count('1'))
        return ans




obj = Solution()
s = "1001"
print(obj.minChanges(s))
