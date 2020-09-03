class Solution(object):
    def recursive(self, A, n, row, col, _sum, ret, last_min): # n fixed
        if row < n and _sum <= last_min:
            _sum += A[row][col]
            if 0 <= col - 1 < n:
                self.recursive(A, n, row + 1, col - 1, _sum, ret, last_min)
            if 0 <= col < n:
                self.recursive(A, n, row + 1, col, _sum, ret, last_min)
            if 0 <= col + 1 < n:
                self.recursive(A, n, row + 1, col + 1, _sum, ret, last_min)    
        else:
            if row == n:
                if _sum not in ret:
                    ret.append(_sum)
                return ret 
        return ret
    
    def minFallingPathSum(self, A):
        min_sum, n = 0, len(A) # width
        ret = []
        
        for i in range(n):
            min_sum += A[i][0]
        for i in range(n): # row
            self.recursive(A, n, 0, i, 0, ret, min_sum)
            min_sum = min(ret, min_sum)
            ret = []
            
            
        return min_sum