class Solution(object):
    def restoreString(self, s, indices):
        ret = [None] * len(s)
        for i, j in zip(list(s), indices):
            ret[j] = i
        return ''.join(ret)