class Solution(object):
    def convertToBase7(self, num):
        abs_num = abs(num)
        ret = ""
        
        while abs_num != 0:
            remainder = abs_num % 7
            ret = str(remainder) + ret
            abs_num = abs_num / 7
        
        if num > 0:
            return ret
        elif num == 0:
            return "0"
        else:
            return "-" + ret
        