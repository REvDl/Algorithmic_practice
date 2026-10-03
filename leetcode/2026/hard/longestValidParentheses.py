

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count = 0
        max_len = 0
        curr_len = 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
                curr_len += 1
            if count < 0:
                count = 0
                curr_len = 0
            if count == 0:
                max_len = max(max_len, curr_len * 2)

        max_two_len = 0
        curr_two_len = 0
        two_count = 0
        for i in range(len(s) -1, -1, -1):
            char = s[i]
            if char == "(":
                two_count -= 1
                curr_two_len += 1
            elif char == ")":
                two_count += 1
            if two_count < 0:
                two_count = 0
                curr_two_len = 0
            if two_count == 0:
                max_two_len = max(max_two_len, curr_two_len * 2)
        return max(max_len, max_two_len)





obj = Solution()
s = ["())()()((()()()))()()()()()()())))(()(())))()()()())(((())))()()()()())))(", "()(()()", "(()", "))))())()()(()"]
for test_char in s:
    print(obj.longestValidParentheses(test_char))
