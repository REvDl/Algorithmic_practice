

class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        dp = [float("inf")] * (n + 1)
        visited = {}
        curr_sum = 0
        left = 0
        ans = float("inf")
        for right in range(n):
            curr_sum += arr[right]
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
            dp[right+1] = dp[right]
            if curr_sum == target:
                ans = min(ans, right - left + 1 + dp[left])
                dp[right+1] =  min(right - left + 1, dp[right])
        return -1 if ans == float("inf") else ans

obj = Solution()
arr = [4,3,2,6,2,3,4,3]
target = 6
print(obj.minSumOfLengths(arr, target))
