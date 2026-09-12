

class Solution:
    #i  thought i could solve this without dp :( (Leetcode task contest 3\4)
    def minDays(self, n: int) -> int:
        days, streak, curr_n = 0, 1, 0
        while True:
            print("HH", curr_n)
            days += 1
            curr_n += streak
            if curr_n < n:
                streak += 1
            elif curr_n > n:
                curr_n -= streak
                streak = 1
            else:
                break
        return days




obj = Solution()
n = 12
print(obj.minDays(n))

