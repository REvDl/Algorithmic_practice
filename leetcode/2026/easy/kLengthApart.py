from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_index = -k - 1
        for i, val in enumerate(nums):
            if val == 1:
                if i - last_index <= k:
                    return False
                last_index = i
        return True

obj = Solution()
nums = [1,0,0,1,0,1]
k = 2
print(obj.kLengthApart(nums, k))


"""
если текущее значени равно 1, начинаем счет от него, как бы это сделать,
инициализируем distance == 0, по идее, а если 0 то += 1, наверно, хотя, что если первым в списке будет не 1 а 0
хм, 
"""