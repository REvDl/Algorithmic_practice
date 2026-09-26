import re

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge = dict(knowledge)
        result = re.sub(r"\(([^)]+)\)", lambda m: knowledge.get(m.group(1), "?"), s)
        return result





obj = Solution()
s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
print(obj.evaluate(s, knowledge))
