# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial


def hexShow(argv):   
    result = ''   
    hLen = len(argv)
    print hLen   
    for i in xrange(hLen):   
        hvol = ord(argv[i])   
        hhex = '%02x'%hvol   
        result += hhex+' '   
    print 'hexShow:',result  

EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.LOW)

ser = serial.Serial("/dev/ttyS0",19200,timeout=0.5)    
# print t.portstr    
# strInput = raw_input('enter some words:')    
# n = t.write(strInput)    
# print n    
# str = t.read(n)    
# print str   

while True:
    print 'listen'
    str = ser.readall()
    # str = raw_input('enter some words:')
    if str:
	    hexShow(str)
    else:
	    print 'no input'    
