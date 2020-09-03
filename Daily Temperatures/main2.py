class Solution(object):
    def dailyTemperatures(self, T):
        _len, right_max = len(T), T[-1]
        ret = [0] * _len
        for i in range(_len - 1, -1, -1):
            if T[i] >= right_max:
                right_max = T[i] # after right_max will be 0
            else:
                j = 1
                while T[i + j] <= T[i]:
                    j += ret[i + j]
                ret[i] = j # days
        return ret