from typing import List



class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //=10   
            result.append(digit_sum)
        return min(result)




obj = Solution()
print(obj.minElement([10, 12, 13, 14]))
