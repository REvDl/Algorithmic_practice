



class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = [num for num in nums if num != val]
        return len(nums)



obj = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(obj.removeElement(nums, val))
