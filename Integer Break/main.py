class Solution(object):
    def integerBreak(self, n):
        dp = [0,0,1] # index 0 = 0, index 1 = 0, index 2 = 1 , it stores "max factors product"
        m = 3 # used to construct dp table
        while m <= n: # dp is getting longer
            max_temp, count = 0, 1 # skip check 0
            while count <= (m // 2):
                factor1 = max(count, dp[count])
                factor2 = max(m - count, dp[m - count])
                max_temp = max(max_temp, factor1 * factor2)         
                count += 1            
            dp.append(max_temp)
            m += 1
        return dp[n]
                
        
        