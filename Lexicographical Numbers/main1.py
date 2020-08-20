class Solution(object):    
    def DFS(self, n, num, _list): # num 是現在在處理的數字
        if num > n:
            return
        _list.append(num)
        if 10 * num <= n:
            self.DFS(n, 10 * num, _list)        
        if num % 10 != 9:
            self.DFS(n, num + 1, _list)   
        return
    def lexicalOrder(self, n):
        _list = []
        self.DFS(n, 1, _list)
        return _list