import RPi.GPIO as GPIO  
import time  
# blinking function  
def blink():  
	# to use Raspberry Pi board pin numbers  
	GPIO.setmode(GPIO.BCM)  
	# set up GPIO output channel  
	GPIO.setup(17, GPIO.OUT)  
        GPIO.output(17,True)  
        time.sleep(1)  
        GPIO.output(17,False)  
        time.sleep(1)
	GPIO.cleanup()    

