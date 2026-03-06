class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag = False
        for i in range(1, len(s)):
            if s[i] == "0":
                flag = True
            if s[i] == "1" and flag:
                return False
        return True