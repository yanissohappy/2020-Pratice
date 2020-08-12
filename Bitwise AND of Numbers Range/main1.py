class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        if n == 0 or m == 0:
            return 0
        while n > m:
            n = n & (n - 1)
        return n
            
        