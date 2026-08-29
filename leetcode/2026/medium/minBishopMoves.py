

class Solution:
    def minBishopMoves_v(self, source: list[int], target: list[int]) -> int:
        s1, s2 = source
        t1, t2 = target
        sum_source = s1 + s2
        sum_target = t1 + t2
        if (sum_source % 2 == 0 and sum_target % 2 != 0) or (sum_source % 2 != 0 and sum_target % 2 == 0):
            return -1
        if sum_source == sum_target or abs(s1 - t1) == abs(s2 - t2):
            return 1
        return 2


obj = Solution()
source = [7,1]
target = [8,2]
print(obj.minBishopMoves_v(source, target))

