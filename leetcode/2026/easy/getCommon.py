from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums2 = set(nums2)
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                return nums1[i]
        else:
            return -1



obj = Solution()
nums1 = [1, 2]
nums2 = [2, 4]
print(obj.getCommon(nums1, nums2))
