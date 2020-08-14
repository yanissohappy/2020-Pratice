class Solution(object):
    def checkPossibility(self, nums):
        non_decreasing_times = 0
        if len(nums) <= 2: 
            return True
        else:
            for i in range(len(nums) - 1):
                if not(nums[i] <= nums[i + 1]):
                    non_decreasing_times += 1
                    if i == 0:
                        nums[i] = nums[i + 1]
                    if i > 0 and nums[i - 1] <= nums[i + 1] : # 判斷值要換前還是換後
                        nums[i] = nums[i + 1]
                    else:
                        nums[i + 1] = nums[i]                        
                    
                if non_decreasing_times > 1:
                    return False
        return True
            
            