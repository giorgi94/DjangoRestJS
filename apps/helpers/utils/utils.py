import datetime as dt
import pytz


a = pytz.utc.localize(dt.datetime.now()).astimezone(tz=pytz.timezone('Asia/Tbilisi'))
b = dt.datetime.strptime('2018-03-09 15:00:05 +0400', '%Y-%m-%d %H:%M:%S %z')

print(a.strftime('%Y-%m-%d %H:%M:%S %z'))
print(b.strftime('%Y-%m-%d %H:%M:%S %z'))
