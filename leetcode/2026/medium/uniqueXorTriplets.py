from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        return 1 << (n.bit_length())


obj = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(obj.uniqueXorTriplets(nums))
