from datetime import datetime
from datetime import timedelta

b=2
z=timedelta(hours=b) + timedelta(hours=-3)
print z
s=str(z)
y = s.split(' ')
print y
time= y[2]
print time
hour=time.split(":")
print hour
req_hour=hour[0]
print req_hour
