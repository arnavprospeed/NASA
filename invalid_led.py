import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
def invalid():
	for i in range(5000):
		GPIO.output(7,True) ## Turn on GPIO pin 7
	GPIO.output(7,False)
