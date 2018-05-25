# 常见的python模块

# from datetime import datetime #表示导入datetime模块的datetime类
import datetime

now = datetime.datetime.now()  # 获取当前时间,now方法返回的是当前的日期与时间
print(now)
print(type(now))

dt = datetime.datetime(2018,5,15,16,51,48,999997)
print(dt.timestamp()) #单位是秒
#timestamp-->datetime

t=dt.timestamp()
print(datetime.datetime.fromtimestamp(t))
#timestamp得到的时间没有时区,fromtimestamp方法得到的时间是有时区的,表示本地时间
#timestamp-->utc标准时区的时间
print(datetime.datetime.utcfromtimestamp(t))

#str-->datetime datetime.strptime()

cday= datetime.datetime.strptime('2018-05-15 08:51:33','%Y-%m-%d %H:%M:%S')
print(cday)

sday = now.strftime('%a, %b %d %H:%M')  #a代表周几,b表示月份
print(sday)

print(now+datetime.timedelta(hours=10))
print(now+datetime.timedelta(days=10))
print(now+datetime.timedelta(hours=10,days=5))

#UTC时间指UTC+0:00时区的时间

#创建时区utc+8:00
tz_utc_8 = datetime.timezone(datetime.timedelta(hours=8))








