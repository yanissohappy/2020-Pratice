class Solution(object):
    def sortAscendBasedOnKorder(self, people):
        """
        height = []
        for a in people:
            if a[0] not in height:
                height.append(a[0])
        left, right = 0, 0
        i = 0
        for h in height:
            while i < len(people):
                if people[i][0] == h:
                    right += 1
                    i += 1
                else:
                    break
            people[left: right].sort(key = lambda x: x[1]) # learnt!!! But I don't know why it doesn't work
            left = right
        """
          
    def reconstructQueue(self, people):
        people.sort(key = lambda x: (-x[0], x[1])) # will sort according to first index descending and second index ascending
        ret = []
        for p in people:
            ret.insert(p[1], p) # according to p[1] to insert in
        return ret
        