

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        term = 0
        res = 0
        for char in s:
            if char == "(":
                stack.append(1)
            else:
                num = stack.pop()
                res += num * 2
        return res




obj = Solution()
s = "(()())"
print(obj.scoreOfParentheses(s))
