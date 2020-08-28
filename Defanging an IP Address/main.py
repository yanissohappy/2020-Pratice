class Solution(object):
    def defangIPaddr(self, address):
        ret = ""
        for char in address:
            if char != ".":
                ret += char
            else:
                ret += "[.]"
        return ret