

class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char in valid:
                if not stack:
                    return False
                if valid[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0


obj = Solution()
print(obj.isValid("[[(]])"))
