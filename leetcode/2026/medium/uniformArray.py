class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        can_even_total = 0
        can_odd_total = 0
        min_num = min(nums1)
        for i in range(n):
            found_even = (nums1[i] % 2 == 0)
            found_odd = (nums1[i] % 2 != 0)
            if nums1[i] - min_num >= 1:
                if (nums1[i] - min_num) % 2 == 0:
                    found_even = True
                if (nums1[i] - min_num) % 2 != 0:
                    found_odd = True
            if found_even: can_even_total += 1
            if found_odd:  can_odd_total += 1
        return can_even_total == n or can_odd_total == n

