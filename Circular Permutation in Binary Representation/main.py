class Solution(object):
    def circularPermutation(self, n, start):
        sequence = [0,1]
        m = 1
        while n > 1: # make sequence
            to_be_added = []
            next_start = 2 ** m
            for i in range(len(sequence)):
                to_be_added.append(sequence[i] + next_start)
            to_be_added = reversed(to_be_added)
            sequence.extend(to_be_added)                
            n -= 1
            m += 1
        
        _index = sequence.index(start)
        ret = sequence[_index:]
        ret.extend(sequence[:_index])
        return ret