from typing import List


class Solution:
    def uniformArray_honest(self, nums1: list[int]) -> bool:
        n = len(nums1)
        can_even_total = 0
        can_odd_total = 0
        for i in range(n):
            found_even = False
            found_odd = False
            for j in range(n):
                if i == j:
                    continue
                if nums1[i] % 2 == 0 or (nums1[i] - nums1[j]) % 2 == 0:
                    found_even = True
                if nums1[i] % 2 != 0 or (nums1[i] - nums1[j]) % 2 != 0:
                    found_odd = True
                if found_even and found_odd:
                    break
            if found_even: can_even_total += 1
            if found_odd:  can_odd_total += 1
        return can_even_total == n or can_odd_total == n


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
