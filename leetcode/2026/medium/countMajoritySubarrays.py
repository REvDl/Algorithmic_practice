from typing import List




class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        prefix_sum[0] = 0
        result = 0
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (-1 if nums[i] != target else 1)
        for i in range(n):
            for j in range(i, n):
                sum_p = prefix_sum[j + 1] - prefix_sum[i]
                if sum_p > 0:
                    result += 1
        return result


obj = Solution()
nums_and_target = {(1,2,2,3): 2, (1,1,1,1): 1}
for nums, target in nums_and_target.items():
    print(obj.countMajoritySubarrays(nums, target))


