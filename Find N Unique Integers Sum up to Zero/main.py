class Solution(object):
    def sumZero(self, n):
        if n & 1 == 0: # even
            ret = []
            neg, pos = -(n / 2), n / 2
            i, j = 0, 0
            while i < pos:
                i += 1
                ret.append(i)
            while neg < j:
                j -= 1
                ret.append(j)
            return ret
        else: # odd
            ret = [0]
            neg, pos = int(-(n / 2)), int(n / 2)
            i, j = 0, 0
            while i < pos:
                i += 1
                ret.append(i)
            while neg < j:
                j -= 1
                ret.append(j)
            return ret            