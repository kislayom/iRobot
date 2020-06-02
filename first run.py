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


gpio.output(ENB,True)
gpio.output(ENA,True)



gpio.output(IN1,False)
gpio.output(IN2,True)

gpio.output(IN3,True)
gpio.output(IN4,False)


time.sleep(6)
gpio.output(ENB,False)
gpio.output(ENA,True)

time.sleep(6)
gpio.output(ENA,False)

