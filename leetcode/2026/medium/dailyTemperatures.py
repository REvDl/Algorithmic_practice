from typing import List


def next_greater_element(arr):
    n = len(arr)
    res = [-1] * n
    stack = []  # индексы
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            res[stack.pop()] = arr[i]
        stack.append(i)
    return res


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


obj = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(next_greater_element(temperatures))
print(obj.dailyTemperatures(temperatures))
