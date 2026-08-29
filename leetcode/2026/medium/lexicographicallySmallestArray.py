from typing import List
from collections import defaultdict, deque


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_sorted = sorted(nums)
        n = len(nums)
        num_to_group = {}
        group = 0
        num_to_group[nums_sorted[0]] = group
        group_list = defaultdict(deque)
        group_list[group] = deque([nums_sorted[0]])
        for i in range(1, n):
            curr_num = nums_sorted[i]
            if abs(nums_sorted[i-1] - curr_num) > limit:
                group += 1
            num_to_group[curr_num] = group
            group_list[group].append(curr_num)

        for i in range(n):
            num = nums[i]
            num_groups = num_to_group[num]
            nums[i] = group_list[num_groups].popleft()
        return nums


obj = Solution()
nums = [1,11,6,2,4,9,14]
limit = 2
print(obj.lexicographicallySmallestArray(nums, limit))
