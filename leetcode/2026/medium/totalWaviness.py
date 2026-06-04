from typing import List


class Solution:

    def checkWaviness(self, num:int) -> int:
        num_s = str(num)
        n = len(num_s)
        wavines = 0
        if n < 3:
            return 0
        for i in range(1, n - 1):
            if num_s[i] > num_s[i - 1] and num_s[i] > num_s[i + 1]:
                wavines += 1
            elif num_s[i] < num_s[i - 1] and num_s[i] < num_s[i + 1]:
                wavines += 1
        return wavines


    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        for num in range(num1, num2 + 1):
            total_waviness += self.checkWaviness(num)
        return total_waviness





obj = Solution()
num1 = 120
num2 = 130
print(obj.totalWaviness(num1, num2))
