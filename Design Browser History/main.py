class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.homepage = homepage
        self.history = [homepage]
        self.now_page = 0 # homepage
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """        
        while len(self.history) > self.now_page + 1:
            self.history.pop()
        self.now_page += 1
        self.history.append(url)

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.now_page - steps <= 0:
            self.now_page = 0
            return self.history[0]
        else:
            self.now_page -= steps
            return self.history[self.now_page]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.now_page + steps >= len(self.history) - 1: # overpass
            self.now_page = len(self.history) - 1
            return self.history[-1]
        else:
            self.now_page += steps
            return self.history[self.now_page]        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)