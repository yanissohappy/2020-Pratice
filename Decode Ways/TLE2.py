class Solution(object):
    def DFS(self, s, num):
        if s[0] == '0':
            return
        if len(s) == 2 and 10 <= int(s[:2]) <= 26: 
            num[0] += 1
            return
        if len(s) == 1 and s[0] != '0':
            num[0] += 1
            return
        if not s:
            num[0] += 1 # 能到這裡表示完整 decode 完一串 string
            return
        
        if len(s) > 1 and 1 <= int(s[:1]) <= 9:
            self.DFS(s[1:], num)
        if len(s) > 2 and 0 < int(s[:2]) <= 26: 
            self.DFS(s[2:], num)
    
    def numDecodings(self, s):
        if s[0] == '0':
            return 0
        num = {0: 0}
        self.DFS(s, num)
        return num[0]
        