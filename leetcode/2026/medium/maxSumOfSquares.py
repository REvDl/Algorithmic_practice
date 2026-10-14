

class Solution:
    def maxSumOfSquares(self, num: int, sum_leetcode: int) -> str:
        nines = "9" * (sum_leetcode // 9)
        remainder = str(sum_leetcode % 9)
        if remainder != '0':
            nines += remainder
        if len(nines) > num:
            return ""
        res = nines.ljust(num, "0")
        return res



obj = Solution()
num = 1
sum_leetcode = 15
print(obj.maxSumOfSquares(num, sum_leetcode))
