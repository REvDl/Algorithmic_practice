from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        max_subsequence = {}
        for num in nums:
            num_in_max = max_subsequence.get(num, 0)
            max_subsequence[num + 1] = num_in_max + 1
            max_subsequence[num] = max(max_subsequence.get(num - 1, 0) + 1, num_in_max)
        return max(max_subsequence.values())


obj = Solution()
nums = [2,1,5,1,1]
print(obj.maxSelectedElements(nums))
