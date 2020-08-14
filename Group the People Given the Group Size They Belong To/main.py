class Solution(object):
    def groupThePeople(self, groupSizes):
        dic = dict(zip(range(0, len(groupSizes)), groupSizes)) # produce array with index
        ret = []
        
        for times in range(1, max(groupSizes) + 1): # find from showup times 1 ~ max(groupSizes)
            if times not in groupSizes:
                continue
            count = 0
            temp = []
            for key, value in dic.items():
                # 如果每次滿了循環就塞入
                if value == times:
                    count += 1
                    temp.append(key)
                if count == times:
                    count = 0
                    ret.append(temp)
                    temp = []
        return ret 