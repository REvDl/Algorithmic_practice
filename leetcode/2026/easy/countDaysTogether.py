

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        get_day = lambda s: sum(days[:int(s[:2]) - 1]) + int(s[3:])
        
        start_a, end_a = get_day(arriveAlice), get_day(leaveAlice)
        start_b, end_b = get_day(arriveBob), get_day(leaveBob)
        
        overlap_start = max(start_a, start_b)
        overlap_end = min(end_a, end_b)
        return max(0, overlap_end - overlap_start + 1)



obj = Solution()
arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
print(obj.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
