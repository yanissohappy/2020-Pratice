class Solution(object):
    def reformatDate(self, date):
        date_list = date.split(' ')
        day = date_list[0][:-2]
        month = date_list[1]
        year = date_list[2]
        
        # adjust
        
        if int(day) < 10:
            day = '0' + day
        _month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        num_month = ""
        for index, mon in enumerate(_month):
            if mon == month:
                num_month = str(index + 1)
        if int(num_month) < 10:
            num_month = '0' + num_month
        
        return year + '-' + num_month + '-' + day