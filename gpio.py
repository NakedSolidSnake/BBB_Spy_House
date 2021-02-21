import Adafruit_BBIO.GPIO as GPIO
import time

lamp = "P8_8"


GPIO.setup(lamp, GPIO.OUT)

def Lamp_setOn():
  GPIO.output(lamp, GPIO.HIGH)


def Lamp_setOff():
  GPIO.output(lamp, GPIO.LOW)
 
