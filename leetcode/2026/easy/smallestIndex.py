from typing import List


class Solution:
    def _sum_num(self, num: int) -> int:
        res = 0
        while num > 0:
            res += num % 10
            num //= 10
        return res


    def smallestIndex(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            res = self._sum_num(num)
            if res == idx:
                return idx
        return -1



obj = Solution()
nums = [1,11,11]
print(obj.smallestIndex(nums))
