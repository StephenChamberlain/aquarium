import os
import glob
import time
import datetime
from database import *

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temperature_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temperature():
    lines = read_temperature_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temperature_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        
        # To calculate fahrenheit...
        #temp_f = temp_c * 9.0 / 5.0 + 32.0
        
        return str(temp_c) #, temp_f
	
def store_temperature_in_db(temperature):
    
    print("Temperature is " + temperature  + " degrees celsius, about to store in DB")
    
    sensorReading = SensorReading.create(
        aquarium=1, 
        reading=str(temperature), 
        reading_units="C", 
        sensor_type="THERMOMETER", 
        timestamp=datetime.datetime.now())
    
    sensorReading.save()
    
print("Starting up")
while True:
    store_temperature_in_db(read_temperature());
    time.sleep(30)
