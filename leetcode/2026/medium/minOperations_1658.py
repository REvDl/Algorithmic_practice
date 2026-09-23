from itertools import product

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        ans = float('inf')
        prefix_sum, suffix_sum = [0] * (n + 1), {}
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        curr_sum = 0
        for i in range(n - 1, -1, -1):
            curr_sum += nums[i]
            suffix_sum[curr_sum] = n - i
        suffix_sum[0] = 0

        for i, p in enumerate(prefix_sum):
            if (x - p) in suffix_sum and i + suffix_sum[x-p] <= n:
                ans = min(ans, suffix_sum[x-p] + i)
        return ans if ans != float('inf') else -1










obj = Solution()
nums =[3,2,20,1,1,3]
x = 10
print(obj.minOperations(nums, x))
