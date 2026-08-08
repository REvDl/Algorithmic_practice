


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = 0
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                res += 1
                i += 1
            j += 1
        return res == len(s)

obj = Solution()
s = "abc"
t = "ahbgdc"
print(obj.isSubsequence(s, t))
