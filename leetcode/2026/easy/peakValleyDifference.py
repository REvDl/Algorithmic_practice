

class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak = 0
        depression = 0
        n = len(nums)
        for i in range(n):
            if (0 < i < n - 1) and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                peak += nums[i]
            elif (0 < i < n - 1) and nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                depression += nums[i]
        return peak - depression


obj = Solution()
nums =[6,5,2,5,5,3,6]
print(obj.peakValleyDifference(nums))
