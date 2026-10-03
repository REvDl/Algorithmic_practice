

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        left_cnt, right_cnt = 0, 0
        for char in s:
            if char == "(":
                left_cnt += 1
            elif char == ")":
                right_cnt += 1
            if right_cnt > left_cnt:
                right_cnt = 0
                left_cnt = 0
            if left_cnt == right_cnt:
                max_len = max(max_len, left_cnt * 2)

        max_two_len = 0
        left_cnt, right_cnt = 0, 0
        for i in range(len(s) -1, -1, -1):
            char = s[i]
            if char == "(":
                left_cnt += 1
            elif char == ")":
                right_cnt += 1
            if left_cnt > right_cnt:
                left_cnt = 0
                right_cnt = 0
            if left_cnt == right_cnt:
                max_two_len = max(max_two_len, left_cnt * 2)
        return max(max_len, max_two_len)

    def longestValidParentheses_v2(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, chr in enumerate(s):
            if chr == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


obj = Solution()
s = ["())()()((()()()))()()()()()()())))(()(())))()()()())(((())))()()()()())))(", "()(()()", "(()", "))))())()()(()"]
for test_char in s:
    print(obj.longestValidParentheses(test_char))
    print("Two solution: ", obj.longestValidParentheses_v2(test_char))
