







class Solution:
    def numberOfSpecialChars_v1(self, word: str) -> int:
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



    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set()
        upper_set = set()
        for char in word:
            if char.isupper():
                upper_set.add(char)
            else:
                lower_set.add(char)
        lower_in_upper = {char.upper() for char in lower_set}
        common_chars = lower_in_upper & upper_set
        return len(common_chars)





obj = Solution()
word = "aaAbcBC"
print(obj.numberOfSpecialChars(word))
