class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 2:
            return nums
        _dict = {}
        
        for i in nums:
            if i not in _dict:
                _dict[i] = 1
            else:
                _dict[i] += 1
            
        ret = []        
        for key, value in _dict.items():
            if value == 1:
                ret.append(key)
        return ret