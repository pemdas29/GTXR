#Given input featherweight data packet,
#extracts Time, Alt, lt, ln data and 
#write to csv file

import pandas as pd
import datetime

#make sure to replace with path to the file!
#Here, FeatherweightPackets is in same directory, though it may not always be 
path = "FeatherweightPackets"

def make_datetime(time):
    return datetime.datetime.strptime (time, "%H:%M:%S.%f")

with open (path, 'r') as f:
    interests = ['Time','Alt', "lt","ln"]
    # rb tells the computer to read bytes
    gps_data = {}
    for i in interests:
        gps_data[i] = list()

    for data in f.readlines():
        if (data.startswith('@ GPS')):
            data = data.split()

            gps_data['Time'].append(make_datetime(data[6]))
            gps_data["Alt"].append(data[data.index('Alt')+1])
            gps_data["lt"].append(data[data.index('lt')+1])
            gps_data['ln'].append(data[data.index('ln')+1])

data = pd.DataFrame(gps_data)
data.to_csv('out.csv')