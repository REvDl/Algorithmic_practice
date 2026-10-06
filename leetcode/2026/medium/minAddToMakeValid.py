

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
                count += 1
            else:
                if stack:
                    stack.pop()
                    count -= 1
                else:
                    count += 1
        return count






obj = Solution()
s = ["()))((", "()(", ")))"]
for char in s:
    print(obj.minAddToMakeValid(char))

