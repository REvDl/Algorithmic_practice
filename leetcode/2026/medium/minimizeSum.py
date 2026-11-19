from typing import List



class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = []
        first, second = nums[0], nums[1]
        nums[0], nums[1] = nums[2], nums[2]
        low_score = float('inf')
        for i in range(n - 1):
            low_score = min(low_score, abs(nums[i + 1] - nums[i]))
        high_score = abs(nums[0] - nums[-1])
        res.append(low_score + high_score)
        nums[0], nums[1] = first, second

        first, second = nums[-1], nums[-2]
        nums[-1], nums[-2] = nums[-3], nums[-3]
        low_score_two = float('inf')
        for i in range(n - 1):
            low_score_two = min(low_score_two, abs(nums[i + 1] - nums[i]))
        high_score_two = abs(nums[0] - nums[-1])
        res.append(low_score_two + high_score_two)
        nums[-1], nums[-2] = first, second

        first, second = nums[0], nums[-1]
        nums[0], nums[-1] = nums[1], nums[-2]
        low_score_three = float('inf')
        for i in range(n - 1):
            low_score_three = min(low_score_three, abs(nums[i + 1] - nums[i]))
        high_score_three = abs(nums[0] - nums[-1])
        res.append(low_score_three + high_score_three)
        return min(res)

obj = Solution()
nums = [[1,4,7,8,5], [1,4,3]]
for num in nums:
    print(obj.minimizeSum(num))

