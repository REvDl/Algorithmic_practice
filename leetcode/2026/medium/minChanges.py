


class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        if s.count('0') == n or s.count('1') == n:
            return 0
        ans = float('inf')
        for i in range(2, n + 1, 2):
            min_sub = []
            for j in range(0, n, i):
                sub = s[j:j+i]
                if '0' in sub and '1' in sub:
                    one_counts, zero_counts = sub.count('1'), sub.count('0')
                    min_sub.append(min(one_counts, zero_counts))
            ans = min(ans, sum(min_sub))
        return ans


obj = Solution()
s = "1001"
print(obj.minChanges(s))
