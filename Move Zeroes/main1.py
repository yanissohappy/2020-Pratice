class Solution(object):
    def moveZeroes(self, nums):
        i, count = 0, 0
        
        while i < len(nums):
            if nums[i] == 0:
                count += 1
                del nums[i]
            else:
                i += 1
                
        nums.extend([0] * count)