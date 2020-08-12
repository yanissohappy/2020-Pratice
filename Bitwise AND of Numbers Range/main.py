class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        left_shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            left_shift += 1
        return m << left_shift
        