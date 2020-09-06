import math
class Solution(object):
    def Cnk(self, n, k):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        ret, ret_reversed = [], []
        if rowIndex & 1 == 1: # odd row
            for i in range((rowIndex + 1) / 2):
                ret.append(self.Cnk(rowIndex, i))
            ret.extend(ret[::-1])
            return ret
        else: # even row
            for i in range(int(rowIndex / 2)):
                ret.append(self.Cnk(rowIndex, i))
            ret_reversed.extend(ret[::-1])
            ret.append(self.Cnk(rowIndex, rowIndex / 2))
            ret.extend(ret_reversed)
            return ret