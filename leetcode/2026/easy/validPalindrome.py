


class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        while left != n:
            res = s[:left] + s[left+1:]
            if res == res[::-1]:
                return True
            left += 1
        return False



obj = Solution()
s = "abca"
print(obj.validPalindrome(s))
