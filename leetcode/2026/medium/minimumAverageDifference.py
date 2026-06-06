from typing import List



class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        n = len(nums)
        left_sum = 0
        min_diff = float('inf')
        best_index = -1
        for i in range(n):
            left_sum += nums[i]
            right_sum  = total_sum - left_sum

            left_avg = (left_sum // (i + i))
            right_avg = (right_sum // (n - i - 1)) if (n - i - 1) > 0 else 0

            current_diff = abs(left_avg - right_avg)
            if current_diff < min_diff:
                min_diff = current_diff
                best_index = i
        return best_index
