class Solution(object):
    def groupAnagrams(self, strs):
        # check len, and every char in a word
        # 方法1: 直接把每個字排列組合然後比對，但如果一個字超長那就絕對不是好方法
        # 方法2: 所以我覺得直接比長度和有沒有每個字的個數都一樣就好
        # 做一個字典list
        
        list_dic = []
        
        for i in range(len(strs)):
            dic = {}
            for j in range(len(strs[i])):
                if strs[i][j] not in dic:
                    dic[ strs[i][j] ] = 1
                else:
                    dic[ strs[i][j] ] += 1                            
            list_dic.append(dic)
        
        rev = []
        
        for i in range(len(list_dic)):
            j = 0
            temp = []
            if list_dic:
                compared_dic = list_dic[0] # save a dictionary model
                temp.append(strs[0])
                del strs[0]
                del list_dic[0]

                while j < len(list_dic):
                    if list_dic[j] == compared_dic:
                        temp.append(strs[j])
                        del strs[j]
                        del list_dic[j]
                        continue
                    j += 1
            if temp:
                rev.append(temp)
        return rev  
            
