

class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            if count < 0:
                return False
        return count == 0

    def removeInvalidParentheses(self, s: str) -> list[str]:
        valid_brackes = set()
        def removeForValid(s: str):
            if self.isValid(s):
                valid_brackes.add(s)
            for i, char in enumerate(s):
                if char not in ["(", ")"]:
                    continue
                substring = s[:i] + s[i+1:]
                removeForValid(substring)
            return
        removeForValid(s)
        res = []
        longest_valid_item = max(valid_brackes, key=lambda x: x.count("(") + x.count(")"))
        need_len = longest_valid_item.count("(") + longest_valid_item.count(")")
        for valid_bracke in valid_brackes:
            if valid_bracke.count("(") + valid_bracke.count(")") == need_len:
                res.append(valid_bracke)
        return res

obj = Solution()
s = "(a)b(c)d(e)f(g"
print(obj.removeInvalidParentheses(s))
