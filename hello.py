from datetime import datetime
from datetime import date
from __future__ import division
from operator import add


blank_day=[0]*24

avg_mon=[0]*24
count_mon=0
sum_mon=[0]*24
z_mon=[0]*25
mon_count=0
avg_num_mon=[]



#Gets the Initial Week of the Year since Power On
while True:
 starting_week= datetime.now().isocalendar()[1]
 print starting_week
 break
 
#Ending week is the last week of Initial Learning Phase.
ending_week= starting_week + 2
print ending_week

#Current week of the Year
current_week= datetime.now().isocalendar()[1]

#Operations carried out during Intital Learning Phase
while current_week<ending_week:
 
    if(datetime.now().hour==1): #Starts at 0AM in the Morning
        #Include 7 hour LED Colour Change
  
    while(datetime.now().isoweekday()==1):   #Monday
        while(#sensor readings true):
            curr_mon= blank_day
            curr_mon[datetime.now().hour]=1
            if(#sensor is false):
                break
        if(datetime.now().isoweekday()!=1):   #Not Monday
            curr_mon=eval(curr_mon)
            count_mon=count_mon+1
            sum_mon=map(add,sum_mon,curr_mon)
            avg_mon = map(lambda w_mon: float(w_mon)/count_mon, sum_mon) #Average of All Mondays.
            list_mon=avg_mon + avg_mon[0:6] # Average 24hour + Average another 6 hour
            x_mon=[list_mon[i_mon:i_mon+7] for i_mon in xrange(0,len(list_mon), 1)] #list having sublists of various combinations
            for sub_mon in x_mon:    #List containing only 7 hour sublists
                if len(sub_mon)==7:
                    y_mon=sub_mon
                    mon_count+=1
                    z_mon[mon_count]=y_mon
            b_mon=z_mon[17:24]+z_mon[1:2]  #List containing sleeping period sublists
            for c_mon in b_mon:
                avg_num_mon+=[sum(c_mon[0:])/len(c_mon[0:])]   #Average of each sleeping period sublists
            max_val_mon = max(avg_num_mon)
            max_index_mon = avg_num.index(max_val_mon) #Index of the Maximum Averaged Sleeping Period Sublist. This index determines start of the Sleep Cycle Lighting schedule
            break
        
       
while current_week>=ending_week:

    while(datetime.now().isoweekday()==1):   #Monday
    
        if(datetime.now().hour)
    
    
        while(#sensor readings true):
            curr_mon= blank_day
            curr_mon[datetime.now().hour]=1
            if(#sensor is false):
                break
        if(datetime.now().isoweekday()!=1):   #Not Monday
            curr_mon=eval(curr_mon)
            count_mon=count_mon+1
            sum_mon=map(add,sum_mon,curr_mon)
            avg_mon = map(lambda w_mon: float(w_mon)/count_mon, sum_mon) #Average of All Mondays.
            list_mon=avg_mon + avg_mon[0:6] # Average 24hour + Average another 6 hour
            x_mon=[list_mon[i_mon:i_mon+7] for i_mon in xrange(0,len(list_mon), 1)] #list having sublists of various combinations
            for sub_mon in x_mon:    #List containing only 7 hour sublists
                if len(sub_mon)==7:
                    y_mon=sub_mon
                    mon_count+=1
                    z_mon[mon_count]=y_mon
            b_mon=z_mon[17:24]+z_mon[1:2]  #List containing sleeping period sublists
            for c_mon in b_mon:
                avg_num_mon+=[sum(c_mon[0:])/len(c_mon[0:])]   #Average of each sleeping period sublists
            max_val_mon = max(avg_num_mon)
            max_index_mon = avg_num.index(max_val_mon) #Index of the Maximum Averaged Sleeping Period Sublist. This index determines start of the Sleep Cycle Lighting schedule
            break
    















