import datetime
import math


now = datetime.datetime.today()

print(now)
print(now.year)
print(now.hour)
print(now.minute)


long_time_ago = datetime.datetime(1999, 3, 14, 12, 30, 58)
print(long_time_ago)

print(long_time_ago < now)


print(math.pi)
