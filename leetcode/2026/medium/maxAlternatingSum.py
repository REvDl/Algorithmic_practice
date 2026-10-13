from typing import List
from functools import wraps
import time
import random


def random_array(start: int, stop: int, size: int) -> list[int]:
    return random.choices(range(start, stop+1), k=size)

def timer(func):
    @wraps(func)
    def wrapper(*args, silent=False, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        execution_time = (end - start) * 1_000_000
        wrapper.execution_time = round(execution_time, 2)
        if not silent:
            print(f'{func.__name__} completed for {wrapper.execution_time}MSC')
        return res
    wrapper.execution_time = None
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
   

    @timer
    def maxAlternatingSum_v3(self, nums: List[int]) -> int:
        squared = sorted(x * x for x in nums)
        n = len(squared)
        left, right = 0, n - 1
        plus = True
        res = 0
        while left <= right:
            if plus:
                res += squared[right]
                right -= 1
            else:
                res -= squared[left]
                left += 1
            plus = not plus
        return res



def reusable_check(range_of: int, obj: Solution, test_case: list[int]):
    result = {
        "v1": [],
        "v2": [],
        "v3": []
    }
    v1_count, v2_count, v3_count = 0, 0, 0
    for _ in range(range_of):
        v1_res = obj.maxAlternatingSum_v1(test_case, silent=True)
        v1_time = obj.maxAlternatingSum_v1.execution_time

        v2_res = obj.maxAlternatingSum(test_case, silent=True)
        v2_time = obj.maxAlternatingSum.execution_time
        
        v3_res = obj.maxAlternatingSum_v3(test_case, silent=True)
        v3_time = obj.maxAlternatingSum_v3.execution_time

        result["v1"].append(f"{v1_time}MSC")
        v1_count += v1_time
        result["v2"].append(f"{v2_time}MSC")
        v2_count += v2_time
        result["v3"].append(f"{v3_time}MSC")
        v3_count += v3_time
    return v1_count / len(result["v1"]), v2_count / len(result["v2"]), v3_count / len(result["v3"])

obj = Solution()
nums = random_array(-4 * 10**4, 4 * 10**4, 10**5)

print(reusable_check(10, obj, nums))
