class Solution(object):
    def bitwiseComplement(self, N):
        if N == 0:
            return 1
        bit_num, ret_N = 0, N
        while N != 0:
            N >>= 1
            bit_num = (bit_num << 1) | 1
        return ret_N ^ bit_num