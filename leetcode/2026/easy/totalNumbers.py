from typing import List
import itertools
from collections import Counter


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


    def totalNumbersMega(self, digits: list[int]) -> int:
        counts = Counter(digits)
        truncated_digits = []
        for digit, count in counts.items():
            truncated_digits.extend([digit] * min(count, 3))
        res = set()
        for digit in itertools.permutations(truncated_digits, 3):
            if digit[0] == 0:
                continue
            num = digit[0] * 100 + digit[1] * 10 + digit[2]
            if num % 2 == 0:
                res.add(num)
        return len(res)


class MyFantasy:
    def totalNumbers(self, digits: List[int]) -> int:
        res = 0
        for digit in itertools.permutations(digits, 3):
            if digit[0] == 0:
                continue
            num = digit[0] * 100 + digit[1] * 10 + digit[2]
            if num % 2 == 0:
                res += num
        return res







obj = Solution()
digits = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5]
print(obj.totalNumbersMega(digits))
