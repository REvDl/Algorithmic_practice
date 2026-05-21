from typing import List


class Solution:
    def longestCommonPrefix_v1(self, arr1: List[int], arr2: List[int]) -> int:
        def prefix_num(number: int) -> List[int]:
            prefix = []
            while number > 0:
                prefix.append(number)
                number //= 10
            prefix.reverse()
            return prefix
        set_prefix = set()
        for i in arr2:
            nums = prefix_num(i)
            for num in nums:
                set_prefix.add(num)
        current_common = 0
        for j in arr1:
            nums = prefix_num(j)
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] in set_prefix:
                    current_common = max(current_common, i + 1)
                    break
        return current_common









obj = Solution()
arr1 = [13,27,45]
arr2 = [21,27,48]
print(obj.longestCommonPrefix_v1(arr1, arr2))



