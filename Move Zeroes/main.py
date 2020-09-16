class Solution(object):
    def moveZeroes(self, nums):
        how_many_zero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0: # 全部非零數往左移
                nums[how_many_zero] = nums[i]
                how_many_zero += 1
        
        for i in range(how_many_zero, len(nums)):
            nums[i] = 0