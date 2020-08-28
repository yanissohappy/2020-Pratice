class Solution(object):
    def kthFactor(self, n, k):
        count = 0
        for i in range(1, int(n / 2) + 1):
            if n % i == 0:
                count += 1
            if count == k:
                return i
            
        count += 1 # the last one
        if count == k:
            return n
        if k > count:
            return -1