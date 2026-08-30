from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        max_idx, min_idx = nums.index(max(nums)), nums.index(min(nums))
        dist_between = abs(max_idx - min_idx) 
        
        first_idx, second_idx = min(max_idx, min_idx), max(max_idx, min_idx)
        second_idx_right = (n - 1) - second_idx

        return min(first_idx + dist_between + 1, second_idx_right + dist_between + 1, first_idx + second_idx_right + 2)



obj = Solution()
nums = [[0,-4,19,1,8,-2,-3,5], [2,10,7,5,4,1,8,6], [-1,1,2,3,4,5,10,6]]
for num in nums:
    print(obj.minimumDeletions(num))
