from typing import List



class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums) 
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for k in range(1, n):
            for i in range(n - k):
                j = i + k
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][n-1] >= 0



obj = Solution()
nums = [1, 567, 1, 1]
print(obj.predictTheWinner(nums))
