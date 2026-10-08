

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = []
        parenthes = ""
        for char in s:
            parenthes += char
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            if count == 0:
                res.append(parenthes.removeprefix("(").removesuffix(")"))
                parenthes = ""
        return "".join(res)


obj = Solution()
s = ["(()())(())(()(()))", "()"]
for char in s:
    print(obj.removeOuterParentheses(char))
