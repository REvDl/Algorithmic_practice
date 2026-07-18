from collections import Counter
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        nod = gcd(len(str1), len(str2))
        return str1[:nod]

obj = Solution()
str1 = "ABABAB"
str2 = "ABAB"
print(obj.gcdOfStrings(str1, str2))
