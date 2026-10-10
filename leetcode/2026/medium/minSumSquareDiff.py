

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        res = 0
        for i in range(n):
            res += (nums1[i] - nums2[i]) ** 2
        return res






obj = Solution()
nums1 = [1,4,10,12]
nums2 =[5,8,6,9]
k1 = 1
k2 = 1
print(obj.minSumSquareDiff(nums1, nums2, k1, k2))
