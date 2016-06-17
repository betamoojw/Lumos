from datetime import datetime
from datetime import date


blank_day=[0]*24
avg_mon=[0]*24
avg_tue=[0]*24
avg_wed=[0]*24
avg_thu=[0]*24
avg_fri=[0]*24
avg_sat=[0]*24
avg_sun=[0]*24


count_mon=0
count_tue=0
count_wed=0
count_thu=0
count_fri=0
count_sat=0
count_sun=0

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
  
 while(datetime.now().isoweekday()==1):
  while(#sensor readings true):
   curr_mon= blank_day
   curr_mon[datetime.now().hour]=1
   if(#sensor is false):
    break
  if(datetime.now().isoweekday()!=1):
   count_mon=count_mon+1
   break

 while(datetime.now().isoweekday()==2):
  while(#sensor readings true):
   curr_tue= blank_day
   curr_tue[datetime.now().hour]=1
   if(#sensor is false):
    break
  if(datetime.now().isoweekday()!=2):
   count_tue=count_tue+1
   break   
   
 while(datetime.now().isoweekday()==3):
  while(#sensor readings true):
   curr_wed= blank_day
   curr_wed[datetime.now().hour]=1
   if(#sensor is false):
    break
  if(datetime.now().isoweekday()!=3):
   count_wed=count_wed+1
   break   
   
 while(datetime.now().isoweekday()==4):
  while(#sensor readings true):
   curr_thu= blank_day
   curr_thu[datetime.now().hour]=1
   if(#sensor is false):
    break
  if(datetime.now().isoweekday()!=4):
   count_thu=count_thu+1
   break  

 while(datetime.now().isoweekday()==5):
  while(#sensor readings true):
   curr_fri= blank_day
   curr_fri[datetime.now().hour]=1
   if(#sensor is false):
    break
  if(datetime.now().isoweekday()!=5):
   count_fri=count_fri+1
   break      
   
 while(datetime.now().isoweekday()==6):
  while(#sensor readings true):
   curr_sat= blank_day
   curr_sat[datetime.now().hour]=1
   if(#sensor is false):
    break
  if(datetime.now().isoweekday()!=6):
   count_sat=count_sat+1
   break   
   
 while(datetime.now().isoweekday()==7):
  while(#sensor readings true):
   curr_sun= blank_day
   curr_sun[datetime.now().hour]=1
   if(#sensor is false):
    break
  if(datetime.now().isoweekday()!=7):
   count_sun=count_sun+1
   break   
   
   
   
