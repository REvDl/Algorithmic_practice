

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        open_bracke = 0
        for char in s:
            if char == "(":
                open_bracke += 1
                count += 1
            else:
                if open_bracke > 0:
                    open_bracke -= 1
                    count -= 1
                else:
                    count += 1
        return count






obj = Solution()
s = ["()))((", "()(", ")))", "()))(())))))(()"]
for char in s:
    print(obj.minAddToMakeValid(char))

