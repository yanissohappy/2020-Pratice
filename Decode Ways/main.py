class Solution(object):
    def DFS(self, s, DP):
        if not s:
            return 1
        if s in DP: 
            return DP[s]
        num1, num2 = 0, 0
        
        if 1 <= int(s[:1]) <= 9:
            num1 = self.DFS(s[1:], DP)
        if len(s) > 1 and 10 <= int(s[:2]) <= 26: 
            num2 = self.DFS(s[2:], DP)      
            
        DP[s] = num1 + num2
        
        return DP[s]
        
    
    def numDecodings(self, s):
        if s[0] == '0':
            return 0
        DP = {}
        return self.DFS(s, DP)
        