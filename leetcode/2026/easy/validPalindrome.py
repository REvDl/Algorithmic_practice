


class Solution:
    def validPalindrome_TLE(self, s: str) -> bool:
        n = len(s)
        left = 0
        while left != n:
            res = s[:left] + s[left+1:]
            if res == res[::-1]:
                return True
            left += 1
        return False


    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                s1 = s[left+1:right+1]
                s2 = s[left:right]
                return s1 == s1[::-1] or s2 == s2[::-1]
        return True


obj = Solution()
s = "abca"
print(obj.validPalindrome(s))
