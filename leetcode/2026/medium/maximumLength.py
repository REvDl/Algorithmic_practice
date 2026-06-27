from typing import List
from collections import Counter



class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        max_subset = 0
        if 1 in frequency:
            count_one = frequency[1]
            max_subset = count_one if count_one % 2 != 0 else count_one - 1
        for x in frequency:
            if x == 1:
                continue
            current_subset = 0
            num = x
            while frequency[num] >= 2:
                current_subset += 2
                num = num ** 2
            if frequency[num] >= 1:
                current_subset += 1
            else:
                current_subset -= 1
            max_subset = max(max_subset, current_subset)
        return max_subset
                



obj = Solution()
nums = [1, 3, 2, 4]
print(obj.maximumLength(nums))
