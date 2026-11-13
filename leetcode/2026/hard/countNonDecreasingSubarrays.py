from typing import List
from collections import deque




class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        res = 1
        n = len(nums)
        left, right = n - 2, n - 1
        queue = deque([[nums[right], 1]])
        while left >= 0:
            counts_num = 1
            while queue and nums[left] > queue[0][0]:
                num, counts = queue.popleft()
                diff = (nums[left] - num) * counts
                counts_num += counts
                k -= diff
            queue.appendleft([nums[left], counts_num])
            while k < 0:
                k += queue[-1][0] - nums[right]
                right -= 1
                if queue[-1][1] > 1:
                    queue[-1][1] -= 1
                else:
                    queue.pop()
            res += right - left + 1
            left -= 1
        return res


obj = Solution()
nums = [6,3,1,2,4,4]
k = 7
print(obj.countNonDecreasingSubarrays(nums, k))
