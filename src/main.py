# main file for running the car 

#Importing modules 
import movement 
import sensors 
import modes 
from machine import Pin
from time import sleep_ms 


def ready_indicator():
    led = Pin("LED", Pin.OUT)
    for i in range(5)
        led.on()
        sleep_ms(500)
        led.off() 
        sleep_ms(500)

ready_indicator() 

def main():
    pass 
