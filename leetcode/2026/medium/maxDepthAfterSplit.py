

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        open_brace = False
        closed_brace = False
        res = []
        for char in seq:
            if char == "(" and open_brace:
                res.append(1)
                open_brace = False
            elif char == "(" and not open_brace:
                res.append(0)
                open_brace = True
            elif char == ")" and closed_brace:
                res.append(1)
                closed_brace = False
            elif char == ")" and not closed_brace:
                res.append(0)
                closed_brace = True
        return res



obj = Solution()
seq = "(()())"
print(obj.maxDepthAfterSplit(seq))
