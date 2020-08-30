class Solution(object):
    def evenSum(self, A):
        _sum = 0
        for i in A:
            if i & 1 == 0:
                _sum += i
        return _sum
    def sumEvenAfterQueries(self, A, queries):
        ret = []
        for i in range(len(queries)):
            A[queries[i][1]] += queries[i][0]
            ret.append(self.evenSum(A))
        return ret