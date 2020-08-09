class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            ret = [[1],[1,1]]

            for i in range(2, numRows):
                temp = [1]
                for j in range(1, i):
                    temp.append(ret[i - 1][j - 1] + ret[i - 1][j])
                temp.append(1)    
                ret.append(temp)

            return ret

        