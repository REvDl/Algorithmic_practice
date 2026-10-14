

class Solution:
    def maxSumOfSquares(self, num: int, sum_leetcode: int) -> str:
        len_sum = len(str(sum_leetcode))
        if num < len_sum:
            return ""
        res = ""
        while True:
            if sum_leetcode > 9:
                res += "9"
                sum_leetcode -= 9
            else:
                res += str(sum_leetcode)
                break
        if len(res) > num:
            return ""
        while len(res) < num:
            res += "0"
        return res


obj = Solution()
num = 2
sum_leetcode = 19
print(obj.maxSumOfSquares(num, sum_leetcode))
