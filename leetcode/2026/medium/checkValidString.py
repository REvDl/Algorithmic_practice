

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_open = []
        stack_stars = []
        count = 0
        for i, chr in enumerate(s):
            if chr == "(":
                stack_open.append(i)
            elif chr == "*":
                stack_stars.append(i)
            elif chr == ")":
                if stack_open:
                    stack_open.pop()
                elif stack_stars:
                    stack_stars.pop()
                else:
                    return False
        while stack_open and stack_stars:
            idx_open = stack_open.pop()
            idx_stars = stack_stars.pop()
            
            if idx_stars > idx_open:
                continue
            else:
                return False
        return True if not stack_open else False


obj = Solution()
s = "("
print(obj.checkValidString(s))
