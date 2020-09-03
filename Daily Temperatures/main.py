class Solution(object):
    def dailyTemperatures(self, T):
        ret = []
        for i in range(len(T)):
            for j in range(i + 1, len(T)):
                if T[j] > T[i]:
                    ret.append(j - i)
                    break
                if j == len(T) - 1:
                    ret.append(0)
        ret.append(0) # there won't be warmer day for the last day
        return ret