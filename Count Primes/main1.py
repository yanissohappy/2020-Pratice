class Solution(object):
    def countPrimes(self, n):
        not_prime = [False] * (n + 1)
        count = 0
        
        for i in range(2, int(n ** 0.5) + 1): # 做到 n ^ (1/2) 的因數即可
            if not not_prime[i]:
                j, multiplicand, multiplier = 0, i, 2
                while j < n + 1:
                    not_prime[j] = True
                    j = multiplicand * multiplier
                    multiplier += 1
                         
        return not_prime[2:n].count(False)
        