

class Solution:
    def countCommas_v1(self, n: int) -> int:
        one_comma = max(n - 999, 0)
        two_comma = max(n - 999_999, 0)
        three_comma = max(n - 999_999_999, 0)
        fourth_comma = max(n - 999_999_999_999, 0)
        five_comma = max(n - 999_999_999_999_999, 0)
        return one_comma + two_comma + three_comma + fourth_comma + five_comma


    def countCommas(self, n: int) -> int:
        diff_numbers = [
            999, 
            999_999, 
            999_999_999,
            999_999_999_999, 
            999_999_999_999_999, 
            999_999_999_999_999_999
                        ]
        return sum([max(n - num_for_diff, 0) for num_for_diff in diff_numbers]


obj = Solution()
nums = [
    100_000,
    100_000_000,
    100_000_000_000
]
for n in nums:
    print(obj.countCommas(n))
