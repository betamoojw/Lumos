from datetime import datetime
import pprint
import json
import os, sys

############################3
## Put the RPi code here
# import RPi.GPIO
def read_sensor():
    reading = True
    return reading
###########################3



class data:
    def __init__(self, load = None):
        self.cur_date = datetime.now()
        if not load:

            self.database = {}
            self.current_datetime = datetime.now()
            
            self.database[self.current_datetime.year] = {}        # add the current year
            
            ######## add current month to first recorded year   ######## 
            self.database[self.current_datetime.year][self.current_datetime.month] = {}

            ######## add current day to first recorded month and put default values for sleep(not sleeping)  ######## 
            self.database[self.current_datetime.year][self.current_datetime.month][self.current_datetime.day] = [None]*24

            pprint.pprint(self.database)
        else:
            # put load code here
            pass
    
    def handle_date_changes(self):
        prev_datetime = self.current_datetime 
        self.current_datetime = datetime.now()
        
        if self.current_datetime - prev_datetime > 320994339248302:   # add something regarding the datetime class, like half hour diff
            pass

    def update_state(self):



        y, m, d = self.current_datetime.isocalendar()    # for getting a  YYYY, MM, DD tuple
        h = self.current_datetime.hour
        if not self.database[y][m][d][h]:
            self.database[y][m][d][h] = read_sensor()

        
    
    def maintain():
        if cur_date < 1212:     # pass
            pass
        pass

data_set = data()




def learning():
    pass

def normal():
    pass


if not os.path.isfile("doze_data.json"):
    is_learning_now = True;
else:
    is_learning_now = False;

cur_sensor_op = None
while True:
    cur_datetime = datetime.now()
    hour = 12
    cur_sensor_op = read_sensor()








