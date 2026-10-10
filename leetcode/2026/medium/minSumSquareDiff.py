from collections import Counter


class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        k = k1 + k2
        if sum(diffs) <= k:
            return 0
        counts = Counter(diffs)

        for num in range(max(diffs), 0, -1):
            if counts[num] == 0:
                continue
            cnt = counts[num]
            if k >= cnt:
                counts[num] = 0
                counts[num-1] += cnt
                k -= cnt
            else:
                counts[num] -= k
                counts[num-1] += k
                break
        return sum(cnt * (num ** 2) for num, cnt in counts.items())





obj = Solution()
nums1 = [1,4,10,12]
nums2 =[5,8,6,9]
k1 = 1
k2 = 1
print(obj.minSumSquareDiff(nums1, nums2, k1, k2))
