class CustomStack(object):

    def __init__(self, maxSize):
        self.maxsize = maxSize
        self.stack = []

    def push(self, x):
        if len(self.stack) < self.maxsize:
            self.stack.append(x)
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k, val):
        for i in range(k):
            if i < len(self.stack):
                self.stack[i] += val
            else:
                break


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)