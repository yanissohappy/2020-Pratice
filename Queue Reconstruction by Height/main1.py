class Solution(object):
    def sortAscendBasedOnKorder(self, people):
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
            a_part_sorted = people[left: right]
            a_part_sorted.sort(key = lambda x: x[1]) # learnt!!! But I don't know why it doesn't work
            people[left: right] = a_part_sorted
            left = right
          
    def reconstructQueue(self, people):
        people.sort(reverse = 1) # will sort according to first index descending and second index ascending
        self.sortAscendBasedOnKorder(people)
        ret = []
        for p in people:
            ret.insert(p[1], p) # according to p[1] to insert in
        return ret
        