# movement for the motors

from machine import Pin, PWM 

class Motor:
    MIN_DUTY = 15000
    MAX_DUTY = 65636

    def __init__(self, pin1, pin2, PWM_pin, speed=0):
        self.pin1 = Pin(pin1, Pin.OUT) 
        self.pin2 = Pin(pin2, Pin.OUT)
        self.PWM_pin = PWM(Pin(PWM_pin))
        #self.duty = duty_u16(0)
        
        self.speed = 0

    def go_forward(self, speed):
        self.pin1.on()
        self.pin2.off()
        self.PWM_pin.freq(duty_u16()

    def go_back(self, speed):


    def turn_right(self):


    def turn_left(self):

    def calc_speed(self, speed):
        if speed <= 0 or speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = duty.speed()
