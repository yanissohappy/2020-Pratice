class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.descending_nums = nums
        # sort
        # though bubble sort is not so good, I still need to practice
        for i in range(len(self.descending_nums) - 1):
            flag = 0 # check if swap
            for j in range(len(self.descending_nums) - 1):
                if self.descending_nums[j] < self.descending_nums[j + 1]:
                    self.descending_nums[j + 1], self.descending_nums[j] = self.descending_nums[j], self.descending_nums[j + 1]
                    flag = 1
            if flag == 0:
                break
            flag = 0
               

    def add(self, val):
        flag = 0
        for i in range(len(self.descending_nums)):
            if val > self.descending_nums[i]:
                self.descending_nums.insert(i, val)
                flag = 1
                break
        if flag == 0:
            self.descending_nums.append(val)
        
        count = 1
        for i in self.descending_nums:
            if self.k == count:
                return i
            count += 1


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)