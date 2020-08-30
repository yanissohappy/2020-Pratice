class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        ret = []
        _sum = 0
        for i in A:
            if i & 1 == 0:
                _sum += i      
        # get all even sum
        for i in range(len(queries)):            
            if queries[i][0] & 1 == 0 and A[queries[i][1]] & 1 == 0: 
                _sum = _sum + queries[i][0]
            elif queries[i][0] & 1 == 0 and A[queries[i][1]] & 1 == 1:
                _sum = _sum 
            elif queries[i][0] & 1 == 1 and A[queries[i][1]] & 1 == 0:
                _sum = _sum - A[queries[i][1]]
            else: # odd + odd
                _sum = _sum + queries[i][0] + A[queries[i][1]]
            A[queries[i][1]] += queries[i][0]
            ret.append(_sum)
        return ret