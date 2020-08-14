class Solution(object):
    def DFS(self,arr, start):
        ans = False
        if arr[start] == 0:
            return True
        if arr[start] == None:
            return False
        
        _next = arr[start]
        arr[start] = None
        if start + _next < len(arr):
            ans |= self.DFS(arr, start + _next)
        if start - _next >= 0:
            ans |= self.DFS(arr, start - _next)
            
        return ans
        
    def canReach(self, arr, start):
        if 0 not in arr:
            return False
        return self.DFS(arr, start)
        
        