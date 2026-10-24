

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day_a = int(arriveAlice[3:])
        day_l = int(leaveAlice[3:])
        month_a = int(arriveAlice[:2])
        month_l = int(leaveAlice[:2])
        day_of_year_a = sum(days[:month_a - 1]) + day_a
        day_of_year_b = sum(days[:month_l - 1]) + day_l
        list_days = [day for day in range(day_of_year_a, day_of_year_b+1)]
        

        bday_a = int(arriveBob[3:])
        bday_l = int(leaveBob[3:])
        bmonth_a = int(arriveBob[:2])
        bmonth_l = int(leaveBob[:2])
        bday_of_year_a = sum(days[:bmonth_a - 1]) + bday_a
        bday_of_year_b = sum(days[:bmonth_l - 1]) + bday_l
        b_list_days = [day for day in range(bday_of_year_a, bday_of_year_b+1)]
        res = sum([1 for day in b_list_days if day in list_days])
        return res



obj = Solution()
arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
print(obj.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
