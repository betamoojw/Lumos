from datetime import datetime
from datetime import date
from operator import add



blank_day=[0]*24
avg_mon=[0]*24

curr_mon=[0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]



count_mon=0
sum_mon=[0]*24



while True:
 curr_mon=raw_input('Enter dat list son')
 curr_mon=eval(curr_mon)
 count_mon=count_mon+1
 print 'Count is',count_mon
 sum_mon=map(add,sum_mon,curr_mon)
 print 'Sum of mondays',sum_mon
 
 avg_mon = map(lambda x: x/count_mon, sum_mon)
 print 'Average monday',avg_mon
 
 die=raw_input('enter no')
 death=int(die)
 if(death==2):
  break






