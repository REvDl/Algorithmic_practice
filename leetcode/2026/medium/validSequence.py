from typing import List




class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        last = [-1] * (m + 1)
        last[m] = n

        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
        res = []
        j = 0
        chg = False
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                if not chg or i < last[j + 1]:
                    res.append(i)
                    j += 1
            else:
                if not chg and (j == m - 1 or i < last[j + 1]):
                    res.append(i)
                    chg = True
                    j += 1
        return res if len(res) == m else []



obj = Solution()
word1 = "vbcca"
word2 = "abc"
print(obj.validSequence(word1, word2))
