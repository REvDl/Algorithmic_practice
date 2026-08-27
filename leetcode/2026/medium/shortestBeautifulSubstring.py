


class Solution:
    def shortestBeautifulSubstring_V1(self, s: str, k: int) -> str:
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


    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n, left, count = len(s), 0, 0
        res = ""
        for right in range(n):
            if s[right] == "1":
                count += 1
            while count == k:
                current = s[left : right + 1]
                res = current if not res else min(res, current, key=lambda x: (len(x), x))
                if s[left] == "1":
                    count -= 1
                left += 1
        return res



obj = Solution()
s = "000"
k = 1
print(obj.shortestBeautifulSubstring(s, k))
