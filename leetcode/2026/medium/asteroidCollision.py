from typing import List 
from collections import deque






class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
                elif abs(asteroid) > stack[-1]:
                    stack.pop()
                else:
                    break
            else:
                stack.append(asteroid)
        return list(stack)



obj = Solution()
print(obj.asteroidCollision([5,10,-5]))
