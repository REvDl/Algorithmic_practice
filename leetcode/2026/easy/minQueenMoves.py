class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        s1, s2 = source
        t1, t2 = target
        sum_source = s1 + s2
        sum_target = t1 + t2
        if s1 == t1 and s2 == t2:
            return 0
        if s1 == t1 or s2 ==  t2 or sum_source == sum_target or abs(s1 - t1) == abs(s2 - t2):
            return 1
        return 2
