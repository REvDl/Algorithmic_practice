


good_integer = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for good in good_integer:
            if good in num:
                return good
        return ""
