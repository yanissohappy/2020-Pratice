class Solution(object):
    def convert(self, s, numRows):
        if not s:
            return s
        if numRows == 1:
            return s
        
        row = 0
        flag = 0 # 0 代表 柱； 1 代表 中間
        ret_string = []
        
        while row < numRows:
            distance = row
            flag = 0
            if row == 0:
                while distance < len(s): 
                    ret_string.append(s[distance])
                    distance += (numRows - 1 - row) * 2
            elif row == numRows - 1:
                while distance < len(s): 
                    ret_string.append(s[distance])
                    distance += (numRows - 1) * 2
            else:
                while distance < len(s): 
                    if flag == 0: # 代表柱
                        ret_string.append(s[distance])  
                        distance += (numRows - (row + 1)) * 2 # 換到中間的位置                             
                    else: # 代表中間
                        ret_string.append(s[distance])
                        distance += row * 2  # 換到柱的位置          
                    flag = flag ^ 1 # bit xor
            row += 1 
            
        return ''.join(ret_string)
        