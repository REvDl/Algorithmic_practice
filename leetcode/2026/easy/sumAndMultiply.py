


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = []
        while n > 0:
            digit = n % 10
            if digit != 0:
                x.append(digit)
            n //= 10
        number = 0
        for digit in reversed(x):
            number = number * 10 + digit
        return number * sum(x)


obj = Solution()
n = 10203004
print(obj.sumAndMultiply(n))
