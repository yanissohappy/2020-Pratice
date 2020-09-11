class Solution(object):
    def pathInZigZagTree(self, label):
        tree = []
        
        # know which row is label in
        row = 0
        while label >= 2 ** row:
            row += 1
        row -= 1
        
        n = 0
        while n <= row:
            temp = []
            if n & 1 == 0: # even, 正序
                temp.extend(range(2 ** n, 2 ** (n + 1)))         
            else:
                temp.extend(range(2 ** n, 2 ** (n + 1))) 
                temp.reverse()
            tree.extend(temp)            
            n += 1
        
        index = 0
        for i, key in enumerate(tree):
            if key == label:
                index = i
                break
                
        ret = [label]
        while index != 0:
            index = (index - 1) / 2
            ret.insert(0, tree[index])
        return ret