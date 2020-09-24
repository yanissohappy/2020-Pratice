class Solution(object):
    def countSegments(self, s):
        if not s:
            return 0
        count = 0
        in_string = False
        for ss in s:
            if ss == " ":
                in_string = False
                continue
            if ss != " " and not in_string:
                in_string = True
                count += 1
            if ss != " " and in_string:
                continue
        return count