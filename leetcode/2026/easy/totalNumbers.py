from typing import List
import itertools


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res = set()
        for digit in itertools.permutations(digits, 3):
            if digit[0] == 0:
                continue
            num = digit[0] * 100 + digit[1] * 10 + digit[2]
            if num % 2 == 0:
                res.add(digit)
        return len(res)

obj = Solution()
digits = [1,2,3,4]
print(obj.totalNumbers(digits))
