# Initialize blank ideal 24 hr weekdays & weekends
ideal_weekday=[0]*24
ideal_weekend=[0]*24
print ideal_weekday
print ideal_weekend
sleep_hour=1
# Initialize  ideal 24 hr weekdays & weekends
ideal_weekday[:8]=[1]*8
ideal_weekend[:8]=[1]*8
print ideal_weekday
print ideal_weekend

from datetime import datetime
nw = datetime.now()
curr_hrs = nw.hour
print curr_hrs
if curr_hrs==15:  #if sensors work:
 ideal_weekday[15]=1 #ideal_weekday[curr_hrs]=1
 print ideal_weekday
 print ideal_weekend
 
 
from datetime import date
print "WeekDay:"
print datetime.now().isoweekday()
print "Week of the year"
print datetime.now().isocalendar()[1]







