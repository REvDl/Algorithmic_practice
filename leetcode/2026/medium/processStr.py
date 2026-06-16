

class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for chr in s:
            if chr == "*":
                if res:
                    res.pop()
                else:
                    continue
            elif chr == "#":
                res += res
            elif chr == "%":
                res.reverse()
            else:
                res.append(chr)
        return "".join(res)
