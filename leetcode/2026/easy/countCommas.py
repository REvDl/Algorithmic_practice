

class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        res = 0
        for i in range(999, n):
            res += 1
        return res

obj = Solution()
n = 1002
print(obj.countCommas(n))
