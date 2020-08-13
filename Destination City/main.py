class Solution(object):
    def destCity(self, paths):
        former_set, last_set = set(), set()
        for city in paths:
            last_set.add(city[1])
            former_set.add(city[0])
        
        return next(iter((last_set.difference(former_set))))