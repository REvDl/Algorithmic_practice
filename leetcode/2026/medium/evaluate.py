import re

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        res = ""
        kl = dict(knowledge)
        current_key = []
        is_brace = False
        for char in s:
            if char == "(":
                is_brace = True
            elif char == ")":
                res += kl.get("".join(current_key), "?")
                current_key = []
                is_brace = False
            else:
                if is_brace:
                    current_key.append(char)
                else:
                    res += char
        return res




obj = Solution()
s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
print(obj.evaluate(s, knowledge))
