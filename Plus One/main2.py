class Solution(object):
    def plusOne(self, digits):
        char_list = list(map(str,digits))
        number = int(''.join(char_list))
        number += 1
        return list(str(number))