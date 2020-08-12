class Solution(object):
    def runningSum(self, nums):     
        ret = []
        ret.append(nums[0])
        
        i = 0
        while i < len(nums) - 1:
            ret.append(ret[i] + nums[i + 1])
            i += 1
        return ret