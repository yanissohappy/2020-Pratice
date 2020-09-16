class Solution(object):
    def hammingDistance(self, x, y):
        xor = x ^ y
        count = 0
        
        while xor != 0:
            if xor & 1 == 1:
                count += 1
            xor >>= 1
        return count