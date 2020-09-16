class Solution(object):
    def sortArrayByParity(self, A):
        ret = []
        for a in A:
            if a & 1 == 0: # even
                ret.insert(0,a)
            else:
                ret.append(a)
        return ret