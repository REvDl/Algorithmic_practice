from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        prefix_arr = [0] * len(A)
        set_arr = set()
        current_common = 0
        for i in range(len(A)):
            if A[i] in set_arr:
                current_common += 1
            set_arr.add(A[i])
            if B[i] in set_arr:
                current_common += 1
            set_arr.add(B[i])
            prefix_arr[i] = current_common
        return prefix_arr




obj = Solution()
A = [1,3,2,4]
B = [3,1,2,4]
print(obj.findThePrefixCommonArray(A, B))
