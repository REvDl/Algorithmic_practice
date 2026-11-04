from typing import List
from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        costs = []
        window = SortedList()
        left_size = (x + 1) // 2
        right_size = x - left_size

        left_sum = 0
        right_sum = 0
        window = SortedList()
        costs = []

        for i in range(len(nums)):
            val = nums[i]
            window.add(val)
            idx = window.index(val)
            if idx < left_size:
                left_sum += val
                if len(window) > left_size:
                    max_num = window[left_size]
                    left_sum -= max_num
                    right_sum += max_num
            else:
                right_sum += val
            
            if i >= x:
                del_val = nums[i - x]
                del_idx = window.index(del_val)
                window.remove(del_val)
                if del_idx < left_size:
                    left_sum -= del_val
                    if len(window) >= left_size:
                        min_num = window[left_size - 1]
                        right_sum -= min_num
                        left_sum += min_num
                else:
                    right_sum -= del_val

            if i >= x - 1:
                median = window[left_size - 1]
                cost = (right_sum - left_sum) + (left_size - right_size) * median
                costs.append(cost)

        dp = [0] * (n + 1)
        for count in range(1, k + 1):
            next_dp = [float('inf')] * (n + 1)
            for i in range(count * x, n + 1):
                start = i - x
                next_dp[i] = min(next_dp[i - 1], dp[start] + costs[start])
            dp = next_dp
        return dp[n] if dp[n] != float('inf') else -1






obj = Solution()
nums = [5,-2,1,3,7,3,6,4,-1]
x = 3
k = 2
print(obj.minOperations(nums, x, k))
