class Solution(object):
    def groupThePeople(self, groupSizes):
        dic = {}
        ret = []
        for index, show_num_in_group in enumerate(groupSizes):
            if show_num_in_group in dic:
                dic[show_num_in_group] += [index]
            else:
                dic[show_num_in_group] = [index]
        for key in dic:
            for i in range(0, len(dic[key]), key):
                ret.append(dic[key][i:i+key])
        return ret