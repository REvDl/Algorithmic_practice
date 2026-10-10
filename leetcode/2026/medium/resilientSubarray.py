

class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        max_len = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                curr_sub = nums[i:j+1]
                if len(curr_sub) == 1:
                    max_len = max(max_len, 1)
                    continue
                else:
                    curr_sum = sum(curr_sub)
                    if all((curr_sum - num) % k == 0 for num in curr_sub):
                        max_len = max(max_len, len(curr_sub))
        return max_len


obj = Solution()
nums = [2,4,6,3]
k = 2
print(obj.resilientSubarray(nums, k))
