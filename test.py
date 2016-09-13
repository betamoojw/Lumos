from datetime import datetime
from datetime import date
from operator import add
from operator import itemgetter  #Used for calculating index of Maximum Period of Day

blank_mon=[0]*24
sum_mon=blank_mon
count_mon=0

print "Blank Monday: ",blank_mon
#curr_mon=[1,0,2,0,3,0,4,0,5,0,3,0,3,0,2,0,1,0,2,0,1,0,1,0]
curr_mon=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
print "Current Monday",curr_mon


#Gets the Initial Week of the Year since Power On
while True:
    starting_week= datetime.now().isocalendar()[1]
    print "starting_week:",starting_week
    break

#Ending week is the last week of Initial Learning Phase.
ending_week= starting_week + 2
print "ending_week:",ending_week

#Current week of the Year
current_week= datetime.now().isocalendar()[1]
print "current_week:",current_week
#for x in range(0,2,1):
#    curr_mon=raw_input("Enter the day Bitch")
#    curr_mon=eval(curr_mon)
count_mon=count_mon+1
print "Monday Count:",count_mon
sum_mon=map(add,sum_mon,curr_mon)                   #Adds all the Mondays together for each hour
print "Total sum of all Mondays::",sum_mon
avg_mon = map(lambda w_mon: float(w_mon)/count_mon, sum_mon)    #Gets the average of the Mondays for each hour
print "Average Monday::", avg_mon
list_mon=avg_mon + avg_mon[0:6]
print "30 hour Monday::",list_mon



x_mon=filter(lambda x: len(x)==7,[list_mon[i_mon:i_mon+7] for i_mon in xrange(0,len(list_mon), 1)])
print "7 hour MOnday",x_mon
print "Length x_mon",len(x_mon)

z_mon=x_mon[17:24]+x_mon[1:3]     #Sleeping Period from 5pm to 2am
print "Sleeping period",z_mon
print "Length z_mon",len(z_mon)

avg_mon=map(lambda a_mon:sum(a_mon)/7,z_mon)    #Takes Average of Each 7-hour-sleeping Period
print "Average Mondays",avg_mon


max_mon=max(avg_mon)                            #Which Sleeping Period is used the Maximum
print "Maximum Monday",max_mon


best_index=max(enumerate(avg_mon), key=itemgetter(1))[0]
print best_index
