from typing import List


class Solution:
    def uniformArray_v1(self, nums1: list[int]) -> bool:
        len_even, len_odd = 0, 0
        n = len(nums1)
        for i in range(n):
            if nums1[i] % 2 == 0:
                len_even += 1
            else:
                len_odd += 1
            for j in range(i+1,n):
                if (nums1[i] - nums1[j]) % 2 == 0:
                    len_even += 1
                else:
                    len_odd += 1
        return True if len_odd >= n or len_even >= n else False


    def uniformArray_v2(self, nums1: list[int]) -> bool:
        n = len(nums1)
        nums2, nums3 = [], []
        for i in range(n):
            for j in range(i,n):
                if i == j:
                    continue
                if nums1[i] % 2 == 0:
                    nums2.append(nums1[i])
                elif (nums1[i] - nums1[j]) % 2 == 0:
                    nums2.append(nums[i] - nums[j])
                elif (nums[i] - nums[j]) % 2 != 0:
                    nums3.append(nums1[i] - nums1[j])
                else:
                    nums3.append(nums1[i])
        return nums2, nums3

    #fuck this solution
    def uniformArray(self, nums1: list[int]) -> bool:
        return True

obj = Solution()
nums1 = [[2,3], [4,6]]
for num in nums1:
    print(obj.uniformArray_v1(num))
