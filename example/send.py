import RPi.GPIO as GPIO
import serial
import binascii

def hex2Str(argv):
    result = ''   
    hLen = len(argv)
    print hLen   
    for i in xrange(hLen):   
        hvol = ord(argv[i])   
        hhex = '%02x'%hvol   
        result += hhex+' '   
    return result 

def str2Hex(str):
    str = str.replace(' ', '')
    hex_values = ['0x' + str[i:i+2] for i in range(0, len(str), 2)]
    int_values = [int(h, base=16) for h in hex_values]
    return int_values

EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

ser = serial.Serial("/dev/ttyS0",19200,timeout=2)    
# print t.portstr    
# strInput = raw_input('enter some words:')    
# n = t.write(strInput)    
# print n    
# str = t.read(n)    
# print str   

while True:
    str = ser.readall()
    # str = raw_input('enter some words:')
    if str:
        str = hex2Str(str)
        print 'get %s' % str
        str = str2Hex(str)
        print 'write %s' % str
        # ser.write(serial.to_bytes(str))
        ser.write(1)