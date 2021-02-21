import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import subprocess
import time

#sensors 
door_sensor = "P9_12"
window_sensor = "P9_15"
temperature_sensor = "P9_37"

GPIO.setup(door_sensor, GPIO.IN)
GPIO.setup(window_sensor, GPIO.IN)

ADC.setup()


def DoorCheckState():
  door_state = GPIO.input(door_sensor)
  return door_state

def WindowCheckState():
  window_state = GPIO.input(window_sensor)
  return window_state

def TemperatureGet():
  output_read = ADC.read_raw(temperature_sensor)
  temperature = (output_read /  10)
  return temperature

  
