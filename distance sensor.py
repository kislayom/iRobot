import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(8,gpio.OUT)
gpio.setup(10,gpio.IN)


gpio.output(8,False)
time.sleep(2)

gpio.output(8,True)
time.sleep(0.00001)
gpio.output(8,False)

while True:
    while gpio.input(10)==0:
        pulse_start=time.time()

    while gpio.input(10)==1:
        pulse_end=time.time()
        
    distance=(pulse_end-pulse_start)*17150
    distance=round(distance,2)

    print ("Distance ",distance)
    time.sleep(0.05)
    gpio.output(8,True)
    time.sleep(0.000001)
    gpio.output(8,False)




