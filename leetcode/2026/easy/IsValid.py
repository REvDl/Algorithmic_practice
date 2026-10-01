

class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char not in closing_brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                element = stack.pop()
                if closing_brackets[char] != element:
                    return False
        return len(stack) == 0


obj = Solution()
print(obj.isValid("[[(]])"))
