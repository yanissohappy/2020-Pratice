class Solution(object):
    def recursive(self, ret, _str, left_p, right_p, n):
        if len(_str) == n * 2:
            ret.append(_str)
            return
        if left_p < n:
            self.recursive(ret, _str + "(", left_p + 1, right_p, n)
        if right_p < left_p:
            self.recursive(ret, _str + ")", left_p, right_p + 1, n)
        
        
    def generateParenthesis(self, n):
        ret = []
        self.recursive(ret, "", 0, 0, n)
        return ret