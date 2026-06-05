from functools import cache




class Solution_1:
    @cache
    def getWavinessSum(self, position:int, tight:bool, lastDigit:int, secondLastDigit:int, is_leading_zero: bool, count_waves: int, num2:int):
        if position == len(str(num2)):
            return count_waves
        def is_tight(tight: bool, pos:int, num2:int):
            if tight:
                limit = int(str(num2)[pos])
            else:
                limit = 9
            return limit
        limit = is_tight(tight, position, num2)
        waviness = 0
        for digit in range(0, limit+1):
            current_wave = 0
            next_tight = tight and (digit == limit)
            next_leading = is_leading_zero and (digit == 0)
            if not is_leading_zero and lastDigit != -1 and secondLastDigit != -1 and lastDigit > digit and lastDigit > secondLastDigit:
                current_wave = 1
            elif not is_leading_zero and lastDigit != -1 and secondLastDigit != -1 and lastDigit < digit and lastDigit < secondLastDigit:
                current_wave = 1
            waviness += self.getWavinessSum(
                position + 1,
                next_tight,
                digit if not next_leading else -1,
                lastDigit if not next_leading else -1,
                next_leading,
                count_waves + current_wave,
                num2)
        return waviness


    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.getWavinessSum(0, True, -1, -1, True, 0, num2) -  self.getWavinessSum(0, True, -1, -1, True, 0 , num1 - 1i)








class Solution:
    @cache
    def getWavinessSum(self, pos:int, tight:bool, lastDigit:int, secondLastDigit:int, is_leading_zero:bool, count_waves:int, num2:int):
        def is_tight(tight:bool, pos:int, num2:int ):
            if tight:
                limit = int(str(num2)[pos])
            else:
                limit = 9
            return limit
        n = len(str(num2))
        if pos == n:
            return count_waves
        limit = is_tight(tight, pos, num2)
        waviness = 0
        for digit in range(0, limit+1):
            current_w = 0
            next_tight = tight and (digit == limit)
            next_leading = is_leading_zero and (digit == 0)
            if not is_leading_zero and secondLastDigit != -1 and lastDigit != -1:
                if (secondLastDigit < lastDigit > digit) or (secondLastDigit > lastDigit < digit):
                    current_w += 1
            waviness += self.getWavinessSum(
                pos+1,
                next_tight,
                digit if not next_leading else -1,
                lastDigit if not next_leading else -1,
                next_leading,
                count_waves + current_w,
                num2
            )
        return waviness


    def totalWaviness(self, num1: int, num2: int) -> int:
        solve_num1 = self.getWavinessSum(0, True, -1, -1, True, 0, num1 - 1)
        solve_num2 = self.getWavinessSum(0, True, -1, -1, True, 0, num2)
        return solve_num2 - solve_num1


