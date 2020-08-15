class Solution(object):
    def addStrings(self, num1, num2):
        num1, num2 = list(num1), list(num2)
        carry, ret = 0, ""
        while len(num2) > 0 or len(num1) > 0:
            if len(num1) > 0:
                n1 = ord(num1.pop()) - ord('0')
            else:
                n1 = 0
            if len(num2) > 0:
                n2 = ord(num2.pop()) - ord('0')
            else:
                n2 = 0                
            
            temp = n1 + n2 + carry 
            ret = chr((temp % 10) + ord('0')) + ret
            carry = temp / 10
        if carry == 1: 
            ret = '1' + ret
        return ret