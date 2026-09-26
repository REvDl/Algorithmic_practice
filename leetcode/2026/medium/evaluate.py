import re

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kl = dict(knowledge)
        curr_key = []
        res = ""
        brace = False
        for char in s:
            if char == "(":
                brace = True
            elif char == ")":
                res += kl.get("".join(curr_key), "?")
                curr_key = []
                brace = False
            else:
                if brace:
                    curr_key.append(char)
                else:
                    res += char
        return res




obj = Solution()
s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
print(obj.evaluate(s, knowledge))
