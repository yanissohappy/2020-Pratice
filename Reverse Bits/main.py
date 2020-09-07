class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        count = 0
        ret = 0
        while count < 32:
            ret <<= 1
            ret = ret | (n & 1)
            n >>= 1            
            count += 1
        return ret