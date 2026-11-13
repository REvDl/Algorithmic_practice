from typing import List



class Solution:
    def _canMakeNoneDecreasing(self, start: int, end: int, k : int, nums: List[int]) -> bool:
        nums_copy = nums[:]
        for i in range(start, end):
            curr_num = nums_copy[i]
            if curr_num > nums_copy[i + 1] and k > 0:
                diff = min(curr_num - nums_copy[i + 1], k)
                nums_copy[i + 1] += diff
                k -= diff
            if curr_num > nums_copy[i + 1]:
                return False
        return True

    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        for right in range(len(nums)):
            while left <= right and not self._canMakeNoneDecreasing(left, right, k, nums):
                left += 1
            res += (right - left + 1)
        return res



obj = Solution()
nums = [6,3,1,2,4,4]
k = 7
print(obj.countNonDecreasingSubarrays(nums, k))
