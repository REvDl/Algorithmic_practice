from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        target_pos = {}
        hash_map = {}
        for i, num in enumerate(nums):
            curr_num = 0
            for chr in str(num):
                curr_num += int(chr)
            hash_map[num] = curr_num
        sort_nums = sorted(nums, key=lambda x: (hash_map[x], x))
        target_pos = {num: i for i, num in enumerate(sort_nums)}
        res = 0
        i = 0
        n = len(nums)
        while i < n:
            num = nums[i]
            if i != target_pos[num]:
                nums[i], nums[target_pos[num]] = nums[target_pos[num]], nums[i]
                res += 1
            else:
                i += 1
        return res





obj = Solution()
nums = [[37, 100], [22,14,33,7], [18,43,34,16], [30, 10, 20]]
for num in nums:
    print(obj.minSwaps(num))
