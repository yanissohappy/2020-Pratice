class Solution(object):
    def recursive(self, candidates, target, index, temp, ret, _sum):
        for idx, candidate in enumerate(candidates):
            if idx >= index:
                if candidate + _sum < target:
                    temp.append(candidate)
                    self.recursive(candidates, target, idx, temp[:], ret, _sum + candidate)
                    temp.pop()
                elif candidate + _sum == target:
                    temp.append(candidate)
                    ret.append(temp[:])
                else: # >
                    continue
    def combinationSum(self, candidates, target):
        ret = []
        candidates.sort()
        self.recursive(candidates, target, 0, [], ret, 0)
        return ret