import RPi.GPIO as gpio
import time
import random
import decimal
import threading


SERVO_PIN=15

# Set GPIO numbering mode
gpio.setmode(gpio.BOARD)
servo1 = gpio.PWM(SERVO_PIN,50)



def turnSensor():
	servo1.start(0)
	print ("Waiting for 2 seconds")
	time.sleep(2)
	while duty <= 12:
	    servo1.ChangeDutyCycle(duty)
	    time.sleep(.02)
	   # servo1.ChangeDutyCycle(5)
	    #time.sleep(2)
	    duty = duty + 1
	time.sleep(1)
	while duty > 2:
	    servo1.ChangeDutyCycle(duty)
	    time.sleep(.02)
	   # servo1.ChangeDutyCycle(5)
	    #time.sleep(2)
	    duty = duty - 1

	time.sleep(2)
	servo1.stop()

thread1=threading.Thread(target=turnSensor)
thread1.start()


