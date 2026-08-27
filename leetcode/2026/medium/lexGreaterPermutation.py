import itertools


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        strings = []
        for p in itertools.permutations(s):
            res = "".join(p)
            if res > target:
                strings.append(res)
        return "" if not strings else min(strings)


obj = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(obj.lexGreaterPermutation(s, target))
