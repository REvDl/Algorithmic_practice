from collections import deque
from typing import List


phone_map = {
    "2": "abc",  "3": "def",  "4": "ghi",
    "5": "jkl",  "6": "mno",  "7": "pqrs",
    "8": "tuv",  "9": "wxyz"
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        queue = deque([""])
        res = []
        for digit in digits:
            letters = phone_map[digit]
            len_q = len(queue)
            for _ in range(len_q):
                current = queue.popleft()
                for letter in letters:
                    queue.append(current + letter)
        return list(queue)


obj = Solution()
digits = "23"
print(obj.letterCombinations(digits))
