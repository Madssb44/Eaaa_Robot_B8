# main file for running the car 

#Importing modules 
import movement 
import sensors 
import modes 
from machine import Pin
from time import sleep_ms 
import socket

def ready_indicator():
    led = Pin("LED", Pin.OUT)
    for i in range(5):
        led.on()
        sleep_ms(500)
        led.off() 
        sleep_ms(500)

ready_indicator() 

def main():
    HOST = "127.0.0.1"
    PORT = 5000

    with socket.socket(socket.IF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

main()

