import datetime

today = datetime.datetime.now()
stat_day = datetime.datetime(year = 2002, month = 12, day = 7)
no_num = (today - stat_day).days//7+1
