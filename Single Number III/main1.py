class Solution(object):
    def singleNumber(self, nums):
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        
        mask = 1
        while(mask & xor == 0):
            mask = mask << 1
            
        # two condition
        ret_a, ret_b = 0, 0
        for num in nums:
            if mask & num:
                ret_a ^= num
            else:
                ret_b ^= num
        return [ret_a, ret_b]