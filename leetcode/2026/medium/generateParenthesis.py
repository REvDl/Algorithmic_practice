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
        visited = set()
        for brackets in permutations(base_string, n * 2):
            bracke = "".join(brackets)
            if bracke in visited:
                continue
            if self.isValid(bracke):
                res.append(bracke)
                visited.add(bracke)
            else:
                continue
        return res



obj = Solution()
n = 3
print(obj.generateParenthesis(n))
