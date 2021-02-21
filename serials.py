#!/usr/bin/python

import Adafruit_BBIO.UART as UART
import serial

UART.setup("UART1")


ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600, timeout = 0.001)

def initSerial():
  ser.close()
  ser.open()


def receiveByte(lenght):
  byte = ser.read(lenght)
  return byte

#def receiveLine():
#  lineRead = serial.

def write(message):
  ser.write(message);

def close():
  ser.close()
  ser = 0
