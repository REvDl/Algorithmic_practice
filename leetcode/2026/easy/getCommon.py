from typing import List


class Solution:
    def getCommon_set(self, nums1: List[int], nums2: List[int]) -> int:
        nums2 = set(nums2)
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                return nums1[i]
        else:
            return -1
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        one_pointer, two_pointer = 0, 0
        while one_pointer < len(nums1) and two_pointer< len(nums2):
            if nums1[one_pointer] > nums2[two_pointer]:
                two_pointer += 1
            elif nums1[one_pointer] < nums2[two_pointer]:
                one_pointer += 1
            else:
                return nums1[one_pointer]
        return -1





obj = Solution()
nums1 = [1, 2]
nums2 = [2, 4]
print(obj.getCommon(nums1, nums2))
