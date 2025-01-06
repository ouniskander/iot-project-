import time
import RPi.GPIO as GPIO

def main():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.IN)
    GPIO.setup(18,GPIO.IN)
    GPIO.setup(26,GPIO.IN)

    while True:
        if GPIO.input(17):
             print "High"
             time.sleep(1)
        else:
             print "low"
             time.sleep(1)
 while True:
        if GPIO.input(18):
             print "High"
             time.sleep(1)
        else:
             print "low"
             time.sleep(1)
 while True:
        if GPIO.input(26):
             print "High"
             time.sleep(1)
        else:
             print "low"
             time.sleep(1)



    GPIO.cleanup()
