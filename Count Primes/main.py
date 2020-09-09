class Solution(object):
    def countPrimes(self, n):
        test_case, count = 2, 0
        while test_case < n:
            factor, flag = 1, False
            while factor <= test_case // 2:
                if test_case % factor == 0 and factor != 1: # 因為factor從 1 開始，所以要先排除掉1的可能
                    flag = True
                    break
                factor += 1
            if not flag:
                count += 1
            test_case += 1    
        return count