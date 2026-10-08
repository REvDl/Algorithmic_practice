import itertools


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        def generateWays(expression: str):
            if expression.isdigit():
                return [int(expression)]
            res = []
            for idx, char in enumerate(expression):
                if char in "+-*":
                    left_part, right_part = expression[:idx], expression[idx+1:]
                    left_generate = generateWays(left_part)
                    right_generate = generateWays(right_part)
                    for left in left_generate:
                        for right in right_generate:
                            if char == "-":
                                res.append(left - right)
                            elif char == "+":
                                res.append(left + right)
                            else:
                                res.append(left * right)
            return res
        return generateWays(expression)



obj = Solution()
expression = "2*3-4*5"
print(obj.diffWaysToCompute(expression))
