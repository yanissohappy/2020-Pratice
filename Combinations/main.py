class Solution(object):
    def limitedDFS(self, index, n, k, ret, temp):
        if len(temp) == k:
            ret.append(temp)
            return
        for i in range(index, n + 1):
            temp.append(i)
            self.limitedDFS(i + 1, n, k, ret, temp[:])
            temp.pop()
        
    def combine(self, n, k):
        ret = []
        self.limitedDFS(1, n, k, ret, [])
        return ret