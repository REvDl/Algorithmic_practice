from collections import defaultdict



class Solution:
    def minOperations(self, s: str) -> int:
        sort_s = "".join(sorted(s))
        n = len(s)
        if s == sort_s:
            return 0
        if n <= 2:
            return -1
        if s[0] == sort_s[0] or s[-1] == sort_s[-1]:
            return 1
        if s[0] == sort_s[-1] and s[-1] == sort_s[0] and sort_s[0] not in s[1:-1] and sort_s[-1] not in s[1:-1]:
            return 3
        return 2

# 101 100 99
# 101 99 100
# 99 101 100
# 111 111 111 108
# 106 103 103
# 101 100 98 99
# 99 97 98
# 97 98 100

s = "cbarcba"
ord_list = [str(ord(chr)) for chr in s]
print(" ".join(ord_list))



obj = Solution()
s = ["dog", "card", "edc", "oool", "onon", "jgg", "edbc"]
for chr in s:
    print(obj.minOperations(chr))
