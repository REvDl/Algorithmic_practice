import string
from collections import deque

ASCII_LETTERS = string.ascii_lowercase

class Solution:
    def multiply_groups(self, group1: list[str], group2: list[str]) -> list[str]:
        res = []
        for one in group1:
            for two in group2:
                res.append(one + two)
        return res


    def delete_duplicates(self, group1: list[str], group2: list[str]) -> list[str]:
        return list(set(group1) | set(group2))


    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        curr_group = [""]
        res_group = []
        for val in expression:
            if val in ASCII_LETTERS:
                curr_group = self.multiply_groups(curr_group, [val])
            elif val == "{":
                stack.append((res_group, curr_group))
                res_group = []
                curr_group = [""]
            elif val == "}":
                curr_brace = self.delete_duplicates(res_group, curr_group)
                prev_res, prev_group = stack.pop()
                curr_group = self.multiply_groups(prev_group, curr_brace)
                res_group = prev_res
            elif val == ",":
                res_group = self.delete_duplicates(res_group, curr_group)
                curr_group = [""]
        finaly_brace = self.delete_duplicates(res_group, curr_group)
        finaly_brace.sort()
        return finaly_brace
            



obj = Solution()
expression = "{a,b}{c,{d,e}}"
print(obj.braceExpansionII(expression))
