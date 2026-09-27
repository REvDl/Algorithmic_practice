import string


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        curr_str = ""
        res = ""
        for char in s:
            if char == "(":
                stack.append(curr_str)
                curr_str = ""
            elif char == ")":
                prev_str = stack.pop()
                curr_str = prev_str + curr_str[::-1]
            else:
                curr_str += char
        return curr_str







obj = Solution()
s = "(u(love)i)"
print(obj.reverseParentheses(s))
