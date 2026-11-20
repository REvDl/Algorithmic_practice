from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_consecutives = {}
        for num in nums:
            next_x = max_consecutives.get(num, 0)
            prev_x = max_consecutives.get(num - 1, 0)
            max_consecutives[num] = max(prev_x + 1, next_x)
            max_consecutives[num + 1] = next_x + 1
        return max(max_consecutives.values())



obj = Solution()
nums = [1000000,999998,999999,999998,999996,999997,999996,999994,999995,999994,999992,999993,999992,999990,999991,999990,999988,999989,999988,999986,999987,999986,999984,999985,999984,999982,999983,999982,999980,999981,1,1,1,2,2,4,4,5,5,7,7,8,8,10,10,11,11,13,13,14,100,100,102,102,104,104,106,106,108,108,110,110,112,112,114,114,116,116,118,118,120,120,122,122,124,124,126,126,128,128]
print(obj.maxSelectedElements(nums))
