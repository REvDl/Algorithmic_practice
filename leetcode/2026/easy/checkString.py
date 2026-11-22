


class Solution:
    def checkString(self, s: str) -> bool:
        return (last < first) if (first := s.find('b')) != -1 and (last := s.rfind('a')) != -1 else True

obj = Solution()
s = "abab"
print(obj.checkString(s))
