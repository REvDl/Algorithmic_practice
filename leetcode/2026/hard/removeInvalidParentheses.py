

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
        res = set()
        def removeForValid(s: str):
            if self.isValid(s):
                res.add(s)
            for i, char in enumerate(s):
                if char not in ["(", ")"]:
                    continue
                substring = s[:i] + s[i+1:]
                removeForValid(substring)
            return
        removeForValid(s)
        need_len = max(res)
        answer = []
        for valid_string in res:
            if len(valid_string) == need_len:
                answer.append(valid_string)
        return answer


obj = Solution()
s = "()()()()))"
print(obj.removeInvalidParentheses(s))
