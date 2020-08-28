class Solution(object):
    def findErrorNums(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        for num in range(1, len(nums) + 1):
            xor ^= num
        bit = 1
        while (xor & bit) != 1:
            bit <<= 1
        # find arbitrary different set
        xor1, xor2 = 0, 0
        for num in nums:
            if bit & num == 0:
                xor1 ^= num
            else:
                xor2 ^= num
        for num in range(1, len(nums) + 1):
            if bit & num == 0:
                xor1 ^= num
            else:
                xor2 ^= num
        # differentiate
        
        for num in nums:
            if num == xor1: # if duplicate
                return [xor1, xor2]
            if num == xor2:
                return [xor2, xor1]
        