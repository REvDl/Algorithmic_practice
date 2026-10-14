

class Solution:
    def maxSumOfSquares(self, num: int, sum_leetcode: int) -> str:
        len_sum = len(str(sum_leetcode))
        if num < len_sum:
            return ""
        
        need_nines = sum_leetcode // 9
        nines_list = ["9" for _ in range(need_nines)]
        remainder_number = str(sum_leetcode % 9)
        if remainder_number != "0":
            nines_list.append(remainder_number)
        len_nines = len(nines_list)
        if len_nines > num:
            return ""
        while len_nines < num:
            nines_list.append("0")
            len_nines += 1
        return "".join(nines_list)

obj = Solution()
num = 1
sum_leetcode = 9
print(obj.maxSumOfSquares(num, sum_leetcode))
