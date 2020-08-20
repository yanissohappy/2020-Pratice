class Solution(object):
    def toLowerCase(self, str):
        ret = []
        for i in str:
            if ord('A') <= ord(i) <= ord('Z'):
                ret.append(chr(ord(i) - ord('A') + ord('a')))
            else:
                ret.append(i)
        return ''.join(ret)
                
        