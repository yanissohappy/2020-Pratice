class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        ret = [[1]]
        
        for _ in range(1, numRows):
            temp = []
            j = 0
            right_shift = [0] + ret[-1]
            left_shift = ret[-1] + [0]
            for i in right_shift:
                temp.append(i + left_shift[j])
                j += 1
            ret.append(temp)
        return ret
        
        