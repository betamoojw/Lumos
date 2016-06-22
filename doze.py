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
 
    avg_mon = map(lambda x: float(x)/count_mon, sum_mon)
    print 'Average monday',avg_mon

 
 
    list2=avg_mon + avg_mon[0:6]
    x=[list2[i:i+7] for i in xrange(0,len(list2), 1)]
    for sublist in x:
        if len(sublist)==7:
        y=sublist
        count+=1
        z[count]=y
print z
    
    
    die=raw_input('enter no')
    death=int(die)
    if(death==2):
        break






