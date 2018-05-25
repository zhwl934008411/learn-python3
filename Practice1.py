import re
from datetime import datetime,timedelta,timezone
#我不知道这个名字和头像,这是很积极的一步了
def to_timestamp(dt_str):
    re_dt_str = re.compile(r'^(20[0-9][0-9])-(1[0-2]|0[1-9])-'
                           r'(3[0-1]|[1-2][0-9]|0[1-9])\s(2[0-4]|1[0-9]|0[1-9])'
                           r':([0-5]?[0-9]):([0-5]?[0-9])$')
    if(re_dt_str.match(dt_str)):
        print('ok')
        dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
        ts=dt.timestamp()
        print(ts)
    else:
        print('failed')

to_timestamp('2016-04-01 08:33:33')

def to_timestamp2(dt_str, tz_str):
    date = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    result = re.match(r'^UTC([+-])(1[0-2]|[0-9]):\d{2}$',tz_str)
    tz=result.group(1)+result.group(2)
    tz_utc = timezone(timedelta(hours=int(tz)))#创建时区
    date = date.replace(tzinfo=tz_utc) #强制设置为UTC+int(tz)
    return date.timestamp()

print(to_timestamp2('2016-04-01 08:33:33','UTC+6:00'))