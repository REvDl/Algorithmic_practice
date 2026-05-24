from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n
        sorted_index = sorted(range(n), key=lambda x: arr[x])
        for i in sorted_index:
            right_j = i + 1
            dp[i] = 1
            while right_j <= n - 1 and (right_j - i) <= d and arr[right_j] < arr[i]:
                dp[i] = max(dp[i], 1 + dp[right_j])
                right_j += 1
            left_j = i - 1
            while left_j >= 0 and (i - left_j) <= d and arr[left_j] < arr[i]:
                dp[i] = max(dp[i], 1 + dp[left_j])
                left_j -= 1
        return max(dp)




obj = Solution()
arr = [3,3,3,3,3]
d = 2
print(obj.maxJumps(arr, d))
