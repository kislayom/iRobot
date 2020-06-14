#!/usr/bin/python3

import RPi.GPIO as gpio
from picamera import PiCamera
import time
import random
import decimal
import _thread
import iRobot as bot


SERVO_PIN=15

#when to stop
MIN_DIST=50

# Set gpio numbering mode
gpio.setmode(gpio.BOARD)

#Servo
gpio.setup(SERVO_PIN,gpio.OUT)


#Shift register led
#Defines the data bit that is transmitted preferentially in the shiftOut function.
LSBFIRST = 4
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 19      #DS Pin of 74HC595(Pin14)
latchPin  = 21      #ST_CP Pin of 74HC595(Pin12)
clockPin = 23       #CH_CP Pin of 74HC595(Pin11)

#Distance Sensor

TRIG=8
ECHO=10
gpio.setup(TRIG,gpio.OUT)
gpio.setup(ECHO,gpio.IN)
gpio.output(TRIG,False)
time.sleep(.5)

HEADLIGHT=37
gpio.setup(HEADLIGHT,gpio.OUT)


#Motors
ENA=7
IN1=11
IN2=13

ENB=36
IN3=16
IN4=18

distance=0

DISCOLED=False

def headlightOn():
    gpio.output(HEADLIGHT,True)
    
def headlightOff():
    gpio.output(HEADLIGHT,False)
    
def turnSensor():
    servo1.start(0)
    print ("Waiting for 2 seconds")
    time.sleep(2)
    duty=2
    servo1.ChangeDutyCycle(duty)
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
    turnSensorByDegree(7)

def turnSensorByDegree(duty1):
    #servo1 = gpio.PWM(SERVO_PIN,50)
    servo1 = gpio.PWM(SERVO_PIN,50)
    servo1.start(0)
    #servo1.pause()
    time.sleep(0.2)
    #servo1.ChangeDutyCycle(2)
    
    print("turning ",duty1)
    servo1.ChangeDutyCycle(duty1)
    time.sleep(0.7)
    print("done turning")
    servo1.stop()
    


def setupLED():
    gpio.setmode(gpio.BOARD)    # Number gpios by its physical location
    gpio.setup(dataPin, gpio.OUT)
    gpio.setup(latchPin, gpio.OUT)
    gpio.setup(clockPin, gpio.OUT)
    gpio.setup(HEADLIGHT,gpio.OUT)
#shiftOut function, use bit serial transmission. 
def shiftOut(dPin,cPin,order,val):
    for i in range(0,8):
        gpio.output(cPin,gpio.LOW);
        if(order == LSBFIRST):
            gpio.output(dPin,(0x01&(val>>i)==0x01) and gpio.HIGH or gpio.LOW)
        elif(order == MSBFIRST):
            gpio.output(dPin,(0x80&(val<<i)==0x80) and gpio.HIGH or gpio.LOW)
        gpio.output(cPin,gpio.HIGH);

def loopLED():
    global DISCOLED
    while DISCOLED:
#         gpio.output(37,True)
#         time.sleep(.10)
#         gpio.output(37,False)
        x=0x64
        for i in range(0,16):
            gpio.output(latchPin,gpio.LOW)  #Output low level to latchPin
            shiftOut(dataPin,clockPin,LSBFIRST,x)#Send serial data to 74HC595
            gpio.output(latchPin,gpio.HIGH)#Output high level to latchPin, and 74HC595 will update the data to the parallel output port.
            x<<=1# make the variable move one bit to left once, then the bright LED move one step to the left once.
            time.sleep(0.05)
        x=0x80
        for i in range(0,16):
            gpio.output(latchPin,gpio.LOW)
            shiftOut(dataPin,clockPin,LSBFIRST,x)
            gpio.output(latchPin,gpio.HIGH)
            x>>=1
            time.sleep(0.05)

def destroy():   # When 'Ctrl+C' is pressed, the function is executed. 
    gpio.cleanup()


def sonarDistance():
    print("Sonar Thread")
    global distance
    gpio.output(TRIG,True)
    time.sleep(0.0001)
    gpio.output(TRIG,False)
    while True:
        gpio.output(TRIG,True)
        time.sleep(0.00001)
        gpio.output(TRIG,False)
        pulse_start=0
        pulse_end=0
        
        while gpio.input(ECHO)==0:
            pulse_start=time.time()

        while gpio.input(ECHO)==1:
            pulse_end=time.time()
            
        distance=(pulse_end-pulse_start)*17150
        distance=round(distance,2)
        time.sleep(.3)
        
        print(distance)
        
def initMotors():
    print("init")

    # set motor pins
    gpio.setup(ENA,gpio.OUT)
    gpio.setup(IN1,gpio.OUT)
    gpio.setup(IN2,gpio.OUT)
    gpio.setup(ENB,gpio.OUT)
    gpio.setup(IN3,gpio.OUT)
    gpio.setup(IN4,gpio.OUT)


def prepareMove():
    gpio.output(ENB,True)
    gpio.output(ENA,True)
    
def moveStraight():
    #Prepare move
    prepareMove()
    #wheel 1
    gpio.output(IN1,False)
    gpio.output(IN2,True)
    #wheel 2
    gpio.output(IN3,True)
    gpio.output(IN4,False)

def aboutTurn():
    gpio.output(ENB,True)
    gpio.output(ENA,True)
    #wheel 1
    gpio.output(IN1,True)
    gpio.output(IN2,False)
    #wheel 2
    gpio.output(IN3,True)
    gpio.output(IN4,False)
    time.sleep(2)
    halt()

def turnLeft():
    halt()
    gpio.output(IN1,False)
    gpio.output(IN2,True)
    gpio.output(IN3,False)
    gpio.output(IN4,True)
    gpio.output(ENA,True)
    gpio.output(ENB,True)
    time.sleep(.5)
    halt()
    
def turnRight():
    halt()
    gpio.output(IN2,False)
    gpio.output(IN1,True)
    gpio.output(IN4,False)
    gpio.output(IN3,True)
    gpio.output(ENA,True)
    gpio.output(ENB,True)
    time.sleep(.5)
    halt()


def halt():
    gpio.output(ENB,False)
    gpio.output(ENA,False)

def run():
    count=0
    time1=0
    global distance
    while True:
        if distance>MIN_DIST :
            moveStraight()
            time.sleep(0.05)
            halt()
            #print("Distance",distance)
        else:
            halt()
            headlightOn()
            #Check left
            print("Right turn")
            turnSensorByDegree(3)
            time.sleep(1)
            rightDistance=distance
            
            #check Right
            print("Left turn")
            turnSensorByDegree(11)
            time.sleep(1)
            leftDistance=distance
            
            #check Right
            print("Straight turn")
            turnSensorByDegree(7)
            time.sleep(1)
            straightDistance=distance
            
            
            
            print("Left ",leftDistance,"Right ",rightDistance,"straight distance",straightDistance)
            if(straightDistance <MIN_DIST and leftDistance < MIN_DIST and rightDistance<MIN_DIST):
                aboutTurn()
            elif(straightDistance>leftDistance and straightDistance>rightDistance):
                print("no need to turn")
            elif (leftDistance>rightDistance):
                print("turn left")
                turnLeft()
            elif (leftDistance<rightDistance):
                print("turn right")
                turnRight()
            time.sleep(0.5)
            headlightOff()

# camera = PiCamera()
# camera.start_preview(alpha=200)
# camera.resolution = (1920, 1080)
# camera.framerate = 15
# camera.start_preview()
# camera.start_recording('/home/pi/Desktop/video.h264')


def startBot():
    
    setupLED()
    initMotors()
    #thread1=_thread.start_new_thread(turnSensor,())
    #thread2=_thread.start_new_thread(loopLED,())
    thread3=_thread.start_new_thread(sonarDistance,())
    turnSensorByDegree(7)
    time.sleep(2)
    while True:
    #print ("distance ",distance)
        time.sleep(1)

#thread4=_thread.start_new_thread(run,())


# camera.stop_preview()
# camera.stop_recording()



