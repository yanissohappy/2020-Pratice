class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # use DP table to record and avoid needless calculation
        num_row = len(triangle)
        dp = triangle[-1]
        
        if num_row == 0:
            return 0
        
        for i in range(num_row - 2, -1, -1): # start from the last second
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
                
        return dp[0]
                