class Solution(object):
    def letterTohex(self,num):
        if num < 10:
            return str(num)
        elif num == 10:
            return "a"
        elif num == 11:
            return "b"
        elif num == 12:
            return "c"
        elif num == 13:
            return "d"
        elif num == 14:
            return "e"
        else: # num == 15
            return "f"
    
    def toHex(self, num):
        ret = ""
        if num > 0:           
            while num != 0:
                _num = num % 16
                ret = self.letterTohex(_num) + ret
                num /= 16
            return ret
        elif num == 0:
            return "0"            
        else: # num < 0
            num= (2 ** 32) - (-num)
            while num != 0:
                _num = num % 16
                ret = self.letterTohex(_num) + ret
                num /= 16
            return ret        