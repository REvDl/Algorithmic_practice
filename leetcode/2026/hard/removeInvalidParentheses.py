

class Solution:
    def __init__(self):
        self.max_valid_len = 0


    def isValid(self, s: str) -> tuple[int, int] | None:
        count = 0
        count_open = 0
        count_close = 0
        for char in s:
            if char == "(":
                count += 1
                count_open += 1
            elif char == ")":
                count -= 1
                count_close += 1
            if count < 0:
                return None
        return (count_open, count_close) if count == 0 else None

    def removeInvalidParentheses(self, s: str) -> list[str]:
        valid_brackes = set()
        visited = set()
        def removeForValid(s: str, prev_len: int):
            if s in visited:
                return
            visited.add(s)
            if len(s) < self.max_valid_len:
                return
            check = self.isValid(s)
            curr_len = check[0] + check[1] if check is not None else prev_len
            if check is not None:
                curr_len = check[0] + check[1]
                if curr_len < prev_len:
                    return
                elif curr_len > prev_len:
                    self.max_valid_len = max(self.max_valid_len, curr_len)
                    valid_brackes.clear()
                    valid_brackes.add(s)
                else:
                    valid_brackes.add(s)
            for i, char in enumerate(s):
                if char not in ["(", ")"]:
                    continue
                substring = s[:i] + s[i+1:]
                removeForValid(substring, self.max_valid_len)
            return
        removeForValid(s, 0)
        return list(valid_brackes)



obj = Solution()
s = ["(a)b(c)d(e)f(g", "()())()", "()", "((((((a))))))((("]
for char in s:
    print(obj.removeInvalidParentheses(char))
