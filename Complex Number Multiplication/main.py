class Solution(object):
    def complexNumberMultiply(self, a, b):
        a_list, b_list = a.split('+'), b.split('+')
        a_num, a_i, b_num, b_i = int(a_list[0]), int(a_list[1][:-1]), int(b_list[0]), int(b_list[1][:-1]) # [:-1] exclude i
        
        real_part = a_num * b_num - (a_i * b_i) # 實部
        img_part = a_i * b_num + b_i * a_num # 虛部
        
        return str(real_part) + '+' + str(img_part) + 'i' 
        
        