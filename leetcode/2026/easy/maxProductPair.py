

class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        res = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i] > nums[j] and nums[i] + nums[j] == target:
                    res.append((i, j))
        max_prod = float("-inf")
        ans = []
        for pair_idx in res:
            prod = nums[pair_idx[0]] * nums[pair_idx[1]]
            if prod > max_prod:
                ans = [pair_idx[0], pair_idx[1]]
                max_prod = prod
        return ans if ans else [-1, -1]


obj = Solution()
nums = [-3,-1,4,2]
target = 1
print(obj.maxProductPair(nums, target))
