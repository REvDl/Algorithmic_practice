

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        first_brace = False
        second_brace = False
        for char in seq:
            if char == "(" and not first_brace:
                res.append(0)
                first_brace = True
            elif char == ")" and not second_brace:
                res.append(0)
                second_brace = True
            elif char == "(" and first_brace:
                res.append(1)
                first_brace = False
            elif char == ")" and second_brace:
                res.append(1)
                second_brace = False
        return res



obj = Solution()
seq = "(()())"
print(obj.maxDepthAfterSplit(seq))
