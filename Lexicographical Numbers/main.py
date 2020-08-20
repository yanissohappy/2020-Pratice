class Solution(object):
    def until10limit(self, num):
        return int(num // 10) * 10 + 10
    
    def DFS(self, n, num, _list): # num 是現在在處理的數字們
        queue = [i for i in range(num, self.until10limit(num)) if i <= n]
        while queue:
            now = queue.pop(0)
            _list.append(now)
            if 10 * now <= n:
                self.DFS(n, 10 * now, _list)               
        return
    def lexicalOrder(self, n):
        _list = []
        self.DFS(n, 1, _list)
        return _list