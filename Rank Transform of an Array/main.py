class Solution(object):
    def bubbleSort(self, arr):
        for i in range(len(arr) - 2, -1, -1): # max iteration
            j = 0
            is_swap = False
            while j <= i:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    is_swap = True
                j += 1
            if is_swap == False: # terminate
                break
        return arr[:]
    def arrayRankTransform(self, arr):
        copy = arr[:]
        rank_list = self.bubbleSort(list(set(copy))) # get rid of duplicate
        ret, rank = [], 1
        for i in arr:
            ret.append(rank_list.index(i) + 1)
            
        return ret
            