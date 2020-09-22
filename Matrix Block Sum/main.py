class Solution(object):        
    def matrixBlockSum(self, mat, K):
        value = 0
        ret = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                for k1 in range(-K, K + 1):
                    for k2 in range(-K, K + 1):
                        if i + k1 < 0 or i + k1 >= len(mat) or j + k2 < 0 or j + k2 >= len(mat[0]):
                            continue
                        else:
                            value += mat[i + k1][j + k2]
                ret[i][j] = value
                value = 0       
        return ret