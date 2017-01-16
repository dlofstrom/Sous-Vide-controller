import serial
import sys
import datetime

#Enter the COM port as argument

ser = serial.Serial(sys.argv[1], baudrate=9600, timeout=None)
now = datetime.datetime.now()
print str(now)
output = open('log_'+str(now)+'.txt', 'w')

while True:
    if ser.in_waiting():
        output.write(ser.read())

output.close()
