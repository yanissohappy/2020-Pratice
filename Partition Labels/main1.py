class Solution(object):
    def partitionLabels(self, S):
        index, farest_index, ret = 0, 0, []
        while index < len(S):
            left = index
            if S[index] in S[index + 1:]:
                farest_index = S.rfind(S[index])
                while index <= farest_index:
                    if S[index] in S[index + 1:]:
                        farest_index = max(farest_index, S.rfind(S[index]))
                    index += 1
                ret.append(farest_index - left + 1)
                continue
            else: 
                ret.append(1)
            index += 1
        return ret