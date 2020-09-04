class Solution(object):
    def hasGcd(self, numerator, denominator):
        n = 2
        while n <= numerator:
            if numerator % n == 0 and denominator % n == 0:
                return True        
            n += 1
        return False
        
    def simplifiedFractions(self, n):
        ret = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if (j / i) < 1 and (not self.hasGcd(j, i) or j == 1):
                    ret.append(str(j) + "/" + str(i))
        return ret