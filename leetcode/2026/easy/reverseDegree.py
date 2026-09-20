

class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for index, char in enumerate(s):
            res += (ord("z") - ord(char) + 1) * (index + 1)
        return res

obj = Solution()
s = "abc"
print(obj.reverseDegree(s))
