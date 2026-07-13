from typing import List



class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for start in range(1, 9):
            num = start
            new_num = start + 1
            while num <= high and new_num <= 9:
                num = num * 10 + new_num
                if low <= num <= high:
                    res.append(num)
                new_num += 1
        return sorted(res)




obj = Solution()
low = 100
high = 300
print(obj.sequentialDigits(low, high))
