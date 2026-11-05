


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        answer = 0
        n, n2 = len(arr1), len(arr2)
        for i in range(n):
            exist = True
            for j in range(n2):
                if abs(arr1[i] - arr2[j]) <= d:
                    exist = False
                    break
            if exist:
                answer += 1
        return answer



obj = Solution()
arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(obj.findTheDistanceValue(arr1, arr2, d))
