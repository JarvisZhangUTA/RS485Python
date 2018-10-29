import RPi.GPIO as GPIO
import serial
import binascii
import time

from command_helper import CommandHelper

test_command = '01020304050607'

EN_485 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.HIGH)

port = serial.Serial("/dev/ttyS0", 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout=1)

while True:
    GPIO.output(EN_485,GPIO.LOW)
    result = port.readall()
    if result:
        result = CommandHelper.toReadable(result)
        print 'receive %s' % result
        GPIO.output(EN_485,GPIO.HIGH)
        
        print 'send %s' % result
        command = CommandHelper.toWriteable(result)
        port.write( command )
        
        while port.out_waiting > 0:
            print '%s waiting' % port.out_waiting
            time.sleep(0.1)
