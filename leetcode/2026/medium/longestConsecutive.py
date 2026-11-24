from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        max_consecutive = float('-inf')
        for num in set_nums:
            curr_consecutive = 0
            if num - 1 not in set_nums:
                while num + 1 in set_nums:
                    curr_consecutive += 1
                    num += 1
            max_consecutive = max(max_consecutive, curr_consecutive)
        return max(max_consecutive + 1, 0)

obj = Solution()
nums =[1,0,1,2]
print(obj.longestConsecutive(nums))
