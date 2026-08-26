


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        substrings = []
        left = 0
        count = 0
        for i in range(n):
            for j in range(i, n+1):
                substring = s[i:j]
                if substring.count("1") == k:
                    substrings.append(substring)
        return "" if not substrings else min(substrings, key=lambda x: (len(x), x))



obj = Solution()
s = "000"
k = 1
print(obj.shortestBeautifulSubstring(s, k))
