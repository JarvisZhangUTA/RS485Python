import RPi.GPIO as GPIO
import serial
import binascii
import time

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

EN_485 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)

while True:
    GPIO.output(EN_485,GPIO.HIGH)

    serial = serial.Serial("/dev/ttyS0", 19200, timeout=1)
    send_serial.write( str2Hex('00') )
    print 'send 00'

    GPIO.output(EN_485,GPIO.LOW)
    result = serial.readall()

    if result:
        result = hex2Str(result)
        print 'receive %s' % result