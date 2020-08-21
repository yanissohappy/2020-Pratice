class Solution(object):
    def partitionLabels(self, S):
        rightmost = {key: index for index, key in enumerate(S)}
        
        index, left, right, ret = 0, 0, 0, []
        
        while left < len(S):
            index = left
            right = rightmost[S[index]]
            while index <= right:
                right = max(right, rightmost[S[index]])
                index += 1
            ret.append(right - left + 1)
            left = index
        
        return ret
        