class Solution(object):
    def addStrings(self, num1, num2):
        dic_num = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        str_num = "0123456789"
        
        i, j = len(num1) - 1, len(num2) - 1
        sum1, sum2 = 0, 0
        
        weight = 1
        while i >= 0:
            sum1 += dic_num[num1[i]] * weight
            weight *= 10
            i -= 1
        weight = 1
        while j >= 0:
            sum2 += dic_num[num2[j]] * weight
            weight *= 10
            j -= 1
        
        _sum = sum1 + sum2
        ret = ""
        
        if _sum == 0:
            return "0"
        
        while _sum:
            ret = str_num[_sum % 10] + ret
            _sum /= 10
        
        return ret