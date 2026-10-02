from itertools import permutations

class Solution:
    def isValid(self, s: list) -> bool:
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
        res = []
        def generateParent(s: str, open_count: int, closed_count: int):
            nonlocal res
            if len(s) == n * 2:
                if self.isValid(s):
                    res.append(s)
                return
            if open_count >= closed_count:
                generateParent(s + "(", open_count + 1, closed_count)
            if closed_count < open_count:
                generateParent(s + ")", open_count, closed_count + 1)

        generateParent("", 0, 0)
        return res


obj = Solution()
n = 3
print(obj.generateParenthesis(n))
