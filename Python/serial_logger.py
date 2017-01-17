import serial
import sys
import datetime

#Enter the COM port as argument

now = datetime.datetime.now()
now = ''.join([i for i in str(now)[:19] if not i in ' -:'])
print str(now)

ser = serial.Serial(sys.argv[1], baudrate=9600, timeout=None)
output = open('log_'+now+'.txt', 'w')

buf = ''
while True:
    if ser.in_waiting:
        buf += ser.read()
        if buf[-1] == '\n':
            output.write(buf)
            print buf
            buf = ''

output.close()
