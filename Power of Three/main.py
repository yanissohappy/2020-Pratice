class Solution(object):
    def isPowerOfThree(self, n):
        initial = 1
        while initial < n:
            copy = initial
            initial <<= 1
            initial += copy
        
        if initial == n:
            return True
        if initial > n:
            return False