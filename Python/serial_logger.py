import serial
import sys
import datetime

#Enter the COM port as argument

ser = serial.Serial(sys.argv[1], baudrate=9600, timeout=None)
now = datetime.datetime.now()
print str(now)
output = open('log_'+str(now)+'.txt', 'w')

buf = ''
while True:
    if ser.in_waiting:
        buf += ser.read()
        if buf[-1] == '\n':
            output.write(buf)
            print buf
            buf = ''

output.close()
