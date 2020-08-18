class Solution(object):       
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        left, right = 0, nums[0]
        jump = 1
        
        while right < len(nums) - 1:
            max_temp = 0
            for i in range(left, right + 1):
                max_temp = max(max_temp, i + nums[i])
            left = right
            right = max_temp
            jump += 1
        return jump
        
        
        

        