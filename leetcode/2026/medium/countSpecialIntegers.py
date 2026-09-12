from collections import Counter
from collections import defaultdict


#                if all(indices[k] == indices[0] + k * (indices[-1] - indices[0]) // (len(indices) - 1) for k in range(len(indices))):


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        res = 0
        visited = set()
        count = Counter(nums)
        last_seen = {}
        step_info = {}
        for index, num in enumerate(nums):
            if num not in last_seen:
                last_seen[num] = index
                step_info[num] = [0, True]
            else:
                current_step = index - last_seen[num]
                if step_info[num][0] == 0:
                    step_info[num][0] = current_step
                elif step_info[num][0] != current_step:
                    step_info[num][1] = False
                last_seen[num] = index
        indices = {num: (0 if info[1] else -1) for num, info in step_info.items()}
        for num in nums:
            if num not in visited and count[num] >= 3 and indices[num] == 0:
                visited.add(num)
                res += 1
        return res




obj = Solution()
nums = [[1,2,1,2,1,2], [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2]]
for num in nums:
    print(obj.countSpecialIntegers(num))
