from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = [0] + flowerbed + [0]
        for i in range(len(flowers)):
            if flowers[i] == 0:
                if flowers[i - 1] == 0 and flowers[i + 1] == 0:
                    n -= 1
                    flowers[i] = 1
        return True if n == 0 else False



obj = Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(obj.canPlaceFlowers(flowerbed, n))
