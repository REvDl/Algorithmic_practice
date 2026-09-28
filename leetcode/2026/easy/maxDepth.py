

class Solution:
    def maxDepth(self, s: str) -> int:
        max_res = []
        curr_res = 0
        for char in s:
            if char == "(":
                curr_res += 1
            elif char == ")":
                curr_res -= 1
            max_res.append(curr_res)
        return max(max_res)

obj = Solution()
s = "()(())((()()))"
print(obj.maxDepth(s))
