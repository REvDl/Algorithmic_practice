

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        res = 0
        curr = 0
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += last * 2 if last != 0 else 1
        return stack[-1]

obj = Solution()
s = ["()", "()()", "(()())", "(()()())", "(()()(((())(((()))))))"]
for char in s:
    print(obj.scoreOfParentheses(char))
