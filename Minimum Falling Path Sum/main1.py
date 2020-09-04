class Solution(object):
    def minFallingPathSum(self, A):
        n = len(A)
        # dp = [[0] * n] * len(A[0]) # 不可以這樣寫!!!!!!!!!!!!!!!!!!!
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[0][i] = A[0][i]
        
        for i in range(1, n): # row
            for j in range(n): # col
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j] + A[i][j], dp[i - 1][j + 1] + A[i][j]) 
                elif j == n - 1:
                    dp[i][j] = min(dp[i - 1][j - 1] + A[i][j], dp[i - 1][j] + A[i][j])
                else: # middle case
                    dp[i][j] = min(dp[i - 1][j - 1] + A[i][j], dp[i - 1][j] + A[i][j], dp[i - 1][j + 1] + A[i][j])
        return min(dp[-1])