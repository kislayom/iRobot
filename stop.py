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

def sonar():
    print("sonar generation")
    gpio.output(TRIG,True)
    time.sleep(0.00001)
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

def moveBack(time):
    prepareMove()
    #wheel 1
    gpio.output(IN2,False)
    gpio.output(IN1,True)
    #wheel 2
    gpio.output(IN4,True)
    gpio.output(IN3,False)
    sleep(time)
    halt()
    
def turnRightStraight(time):
    halt()
    gpio.output(ENA,True)
    gpio.output(IN1,False)
    gpio.output(IN2,True)
    time.sleep(time)
    halt()
    
def turnLeftStraight(time):
    halt()
    gpio.output(ENB,True)
    gpio.output(IN3,True)
    gpio.output(IN4,False)
    time.sleep(time)
    halt()

def turnRightBack(time):
    halt()
    gpio.output(ENA,True)
    gpio.output(IN2,False)
    gpio.output(IN1,True)
    time.sleep(time)
    halt()
    
def turnLeftBack(time):
    halt()
    gpio.output(ENB,True)
    gpio.output(IN4,True)
    gpio.output(IN3,False)
    time.sleep(time)
    halt()

def run():
 
    halt()

init()
run()







