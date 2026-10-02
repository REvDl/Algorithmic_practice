from itertools import permutations

class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        for char in s:
            if char == "(":
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    def generateParenthesis(self, n: int) -> list[str]:
        base_string = "()" * n
        res = []
        unique_permutations = set("".join(p) for p in permutations(base_string))
        for brake in unique_permutations:
            if self.isValid(brake):
                res.append(brake)
        return res


obj = Solution()
n = 3
print(obj.generateParenthesis(n))
