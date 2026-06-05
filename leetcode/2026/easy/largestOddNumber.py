


odd = "1379"
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) -1, -1, -1):
            chr = num[i]
            if chr in odd:
                return num[:i + 1]
        return ""
