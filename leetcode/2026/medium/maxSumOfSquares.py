

class Solution:
    def maxSumOfSquares(self, num: int, sum_leetcode: int) -> str:
        res = 0
        number = [0] * num
        while True:
            sum_number = sum(number)
            if sum_number == sum_leetcode:
                break
            if sum_number > sum_leetcode:
                return ""
            if len(number) > num:
                return ""
            for i in range(len(number) - 1, -1, -1):
                if number[i] < 9:
                    number[i] += 1
                    break
                else:
                    number[i] = 0
            else:
                number = [1] + number
        return "".join(str(x) for x in number)[::-1]



obj = Solution()
num = 1
sum_leetcode = 10
print(obj.maxSumOfSquares(num, sum_leetcode))
