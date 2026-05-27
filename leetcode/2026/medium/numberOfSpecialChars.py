from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letter_upper = dict()
        letter_lower = dict()
        for idx, val in enumerate(word):
            if val.isupper():
                if val in letter_upper:
                    continue
                letter_upper[val] = idx
            else:
                letter_lower[val] = idx
        result = 0
        for char in letter_lower:
            if char.upper() in letter_upper and letter_lower[char] < letter_upper[char.upper()]:
                result += 1
                
        return result





obj = Solution()
word = "aaAbcBC"
print(obj.numberOfSpecialChars(word))
