class Solution(object):
    def DFS(self, s, num):

        if not s:
            num[0] += 1 # 能到這裡表示完整 decode 完一串 string
            return

        i = 1
        
        while i < len(s) + 1:
            if i < 3:
                if len(s[:i]) >= 2 and s[:i][0] == '0':
                    return
                if i < 3 and 0 < int(s[:i]) <= 26: 
                    self.DFS(s[i:], num)
            else: 
                return
            i += 1
    
    def numDecodings(self, s):
        if s[0] == '0':
            return 0
        num = {0: 0}
        self.DFS(s, num)
        return num[0]
        