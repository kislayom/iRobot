import RPi.GPIO as gpio
import time
import random
import decimal



gpio.setmode(gpio.BOARD)

ENA=7
IN1=11
IN2=13

ENB=36
IN3=16
IN4=18

TRIG=8 #generate sound
ECHO=10 #receive echo

def init():
    print("ïnit")
    #set sensor pins
    gpio.setup(TRIG,gpio.OUT)
    gpio.setup(ECHO,gpio.IN)
    # set motor pins
    gpio.setup(ENA,gpio.OUT)
    gpio.setup(IN1,gpio.OUT)
    gpio.setup(IN2,gpio.OUT)
    gpio.setup(ENB,gpio.OUT)
    gpio.setup(IN3,gpio.OUT)
    gpio.setup(IN4,gpio.OUT)
    
    #reset TRIG
    gpio.output(TRIG,False)
    time.sleep(2)
    print("Trig reset")
    
    gpio.setup(15,gpio.OUT)
    gpio.setup(37,gpio.OUT)
    
    

def sonar():
    print("sonar generation")
    gpio.output(TRIG,True)
    time.sleep(0.0001)
    gpio.output(TRIG,False)
    
def sonarDistance():
    pulse_start=0
    pulse_end=0
    
    while gpio.input(ECHO)==0:
        pulse_start=time.time()

    while gpio.input(ECHO)==1:
        pulse_end=time.time()
        
    distance=(pulse_end-pulse_start)*17150
    distance=round(distance,2)
    return distance

def halt():
    gpio.output(ENB,False)
    gpio.output(ENA,False)
    
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
    time.sleep(20)
    halt()

def moveBack(time1):
    prepareMove()
    #wheel 1
    gpio.output(IN2,False)
    gpio.output(IN1,True)
    #wheel 2
    gpio.output(IN4,True)
    gpio.output(IN3,False)
    time.sleep(time1)
    halt()
    
def turnRightStraight(time1):
    halt()
    gpio.output(ENA,True)
    gpio.output(IN1,False)
    gpio.output(IN2,True)
    time.sleep(time1)
    halt()
    
def turnLeftStraight(time1):
    halt()
    gpio.output(ENB,True)
    gpio.output(IN3,True)
    gpio.output(IN4,False)
    time.sleep(time1)
    halt()

def turnRightBack(time1):
    halt()
    gpio.output(ENA,True)
    gpio.output(IN2,False)
    gpio.output(IN1,True)
    time.sleep(time1)
    halt()
    
def turnLeftBack(time1):
    halt()
    gpio.output(ENB,True)
    gpio.output(IN4,True)
    gpio.output(IN3,False)
    time.sleep(time1)
    halt()

def run():
    count=0
    time1=0
    while True:
        sonar()
        distance=sonarDistance()
        print(distance)
        while distance>50 :
            moveStraight()
            time.sleep(0.5)
            halt()
            sonar()
            distance=sonarDistance()
            print("Distance",distance)
        halt()
        time.sleep(1)
        time1=decimal.Decimal(random.randrange(100, 150))/100
        time1=.65
        functionRand=random.randrange(5)
        
        
        if functionRand==0:
            print("moving back")
            moveBack(0.5)
            time.sleep(0.5)
            turnRightStraight(time1)
        elif functionRand==1:
            print("turn right straight")
            moveBack(0.5)
            time.sleep(0.5)
            turnRightStraight(time1)
        elif functionRand==2:
            print("turn left straight")
            moveBack(0.5)
            time.sleep(0.5)
            turnLeftStraight(time1)
        elif functionRand==3:
            print("turn right back")
            moveBack(0.5)
            time.sleep(0.5)
            turnRightBack(time1)
        elif functionRand==4:
            print("turn left back")
            moveBack(0.5)
            time.sleep(0.5)
            turnLeftBack(time1)
            
        
        sonar()
        distance=sonarDistance()
        halt()
        time.sleep(0.2)
        print(time1, functionRand,distance)
        time.sleep(0.59)
        count=count+1
        if count==5:
            break
    halt()

init()
servo1 = gpio.PWM(15,50)
time.sleep(2)
servo1.ChangeDutyCycle(2)
print("servo done ")
time.sleep(5)
counter=0
moveBack(3)
halt()
time.sleep(10)
run()






