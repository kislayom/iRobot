import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

ENA=7
IN1=11
IN2=13

ENB=36
IN3=16
IN4=18

gpio.setup(ENA,gpio.OUT)
gpio.setup(IN1,gpio.OUT)
gpio.setup(IN2,gpio.OUT)
gpio.setup(ENB,gpio.OUT)
gpio.setup(IN3,gpio.OUT)
gpio.setup(IN4,gpio.OUT)






gpio.output(IN1,False)
gpio.output(IN2,True)

gpio.output(IN3,True)
gpio.output(IN4,False)

time.sleep(1)
gpio.output(ENA,False)
gpio.output(ENB,False)

p=gpio.PWM(ENA,1000)
q=gpio.PWM(ENB,1000)
p.start(0)
q.start(0)
time.sleep(1)
p.ChangeDutyCycle(100)
q.ChangeDutyCycle(100)
gpio.output(ENB,True)
gpio.output(ENA,True)
time.sleep(5)
gpio.output(ENA,False)
gpio.output(ENB,False)

time.sleep(1)

time.sleep(2)
gpio.output(ENA,False)
gpio.output(ENB,False)
p.ChangeDutyCycle(0)
q.ChangeDutyCycle(0)

