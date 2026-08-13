from typing import List
from collections import Counter





class Solution:
    def _get_max_consecutive(self, chars: List[str]) -> int:
        max_len = 0
        current_len = 0
        prev_char = ""
        
        for char in chars:
            if char == prev_char:
                current_len += 1
            else:
                current_len = 1
                prev_char = char
            if current_len > max_len:
                max_len = current_len
        return max_len


    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        k = len(queryCharacters)
        replace_str = list(s)
        result = []
        for idx, char in zip(queryIndices, queryCharacters):
            replace_str[idx] = char
            result.append(self._get_max_consecutive(replace_str))
        return result





obj = Solution()
s = "babacc"
queryCharacters = "bcb"
queryIndices = [1,3,3]
print(obj.longestRepeating(s, queryCharacters, queryIndices))
