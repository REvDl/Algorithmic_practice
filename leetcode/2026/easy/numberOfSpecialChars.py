







class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set()
        upper_set = set()
        result = 0
        for char in word:
            if char.isupper():
                upper_set.add(char)
            elif char.islower():
                lower_set.add(char)
        print(lower_set, upper_set)
        for char in lower_set:
            if char.upper() in upper_set:
                result += 1
        return result

obj = Solution()
word = "aaAbcBC"
print(obj.numberOfSpecialChars(word))
