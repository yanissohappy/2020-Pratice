class Solution(object):
    def diagonalSort(self, mat):
        # mat[num][0]
        # mat[0][num]
        
        for i in range(len(mat)):
            temp_i = i
            temp_j = 0
            temp_list = []
            while temp_i < len(mat) and temp_j < len(mat[0]):
                temp_list.append(mat[temp_i][temp_j])
                temp_i += 1
                temp_j += 1
            temp_list.sort()
            temp_i = i
            temp_j = 0
            while temp_i < len(mat) and temp_j < len(mat[0]):
                mat[temp_i][temp_j] = temp_list.pop(0)
                temp_i += 1
                temp_j += 1            
            
        for j in range(len(mat[0])):
            temp_i = 0
            temp_j = j
            temp_list = []
            while temp_i < len(mat) and temp_j < len(mat[0]):
                temp_list.append(mat[temp_i][temp_j])
                temp_i += 1
                temp_j += 1
            temp_list.sort()
            temp_i = 0
            temp_j = j
            while temp_i < len(mat) and temp_j < len(mat[0]):
                mat[temp_i][temp_j] = temp_list.pop(0)
                temp_i += 1
                temp_j += 1      
        return mat