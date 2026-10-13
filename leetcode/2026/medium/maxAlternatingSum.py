from typing import List
from functools import wraps
import time
import random


def random_array(range_of: int, size: int) -> list[int]:
    return random.sample(range(range_of), size)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        execution_time = (end - start) * 1_000_000
        print(f"{func.__name__} completed for {round(execution_time, 2)}MSC")
        return res
    return wrapper

class Solution:
    @timer
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares_num = sorted(x * x for x in nums)
        mid = len(nums) // 2
        return sum(squares_num[mid:]) - sum(squares_num[:mid]) 

    @timer
    def maxAlternatingSum_v1(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: abs(x))
        n = len(nums)
        res = 0
        for i in range(n):
            if i % 2 == 0:
                index = -1 - (i // 2)
            else:
                index = i // 2
            current_element = nums[index]
            if i % 2 == 0:
                res += (current_element) ** 2
            else:
                res -= (current_element) ** 2
        return res

obj = Solution()
nums = random_array(100000000, 60)
print(obj.maxAlternatingSum(nums + nums + nums + nums))
print(obj.maxAlternatingSum_v1(nums + nums + nums + nums))
