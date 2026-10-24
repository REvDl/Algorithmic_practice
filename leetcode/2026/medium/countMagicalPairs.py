from collections import Counter


class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        res = 0
        for j in range(n - 1):
            s1 = []
            set_s1 = set()
            for i in range(j, -1, -1):
                set_s1.add(s[i])
                s1.append(len(set_s1))
            s2 = []
            set_s2 = set()
            for k in range(j + 1, n):
                set_s2.add(s[k])
                s2.append(len(set_s2))
            c1 = Counter(s1)
            c2 = Counter(s2)
            for unique in c1:
                if unique in c2:
                    res += c1[unique] * c2[unique]
        return res


obj = Solution()
s = "aba"
print(obj.countMagicalPairs(s))
