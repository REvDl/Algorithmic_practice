from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_translate = dict()
        count = 1
        for num in sorted(arr):
            if num not in num_translate:
                num_translate[num] = count
                count += 1
        result = [num_translate[x] for x in arr]
        return result



obj = Solution()
arr = [40,10,20,30]
print(obj.arrayRankTransform(arr))
