class Solution(object):
    def licenseKeyFormatting(self, S, K):
        clear_string = S.upper().replace('-','')
        clear_string = clear_string[::-1] # reverse string
        
        ret_string = ""
        i = 0
        
        while i < len(clear_string):
            if i + K < len(clear_string): # check whether add '-'
                ret_string += clear_string[i : i + K]
                ret_string += "-"
            else: # over len
                break
            i += K
        while i < len(clear_string):
            ret_string += clear_string[i]
            i += 1
        
        return ret_string[::-1]