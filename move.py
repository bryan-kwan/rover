import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)


GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)






GPIO.output(11, GPIO.HIGH)
sleep(2)
GPIO.output(11, GPIO.LOW)

GPIO.cleanup()
print("Exiting")
