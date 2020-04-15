import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)


GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)






GPIO.output(17, GPIO.HIGH)
sleep(2)
GPIO.output(17, GPIO.LOW)
