import math
import time

import Adafruit_CharLCD as LCD

# BeagleBone Black configuration:
lcd_rs        = 'P8_8'
lcd_en        = 'P8_10'
lcd_d4        = 'P8_18'
lcd_d5        = 'P8_16'
lcd_d6        = 'P8_14'
lcd_d7        = 'P8_12'
lcd_backlight = 'P8_7'

lcd_columns = 16
lcd_rows = 2

#Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

def printMessage(message):
  lcd.message(message)

def newLine():
  lcd.message('\n')

def clear():
  lcd.clear()

def cursorSet(cursorOn_Off):
  if cursorOn_Off == True:
    lcd.show_cursor(True)
  else:
    lcd.show_cursor(False)

def initialScreen():  
  message_welcome = "Smart House\n"
  version = "1.0.0"
  #lcd.message(message_welcome)
  #lcd.message(version)
  printCenter(message_welcome)
  printCenter(version)
  time.sleep(2)

def printCenter(message):
   lenght = len(message)
   differ = (16 - lenght) / 2
   for num in range(0, differ):
     lcd.message(' ');
   lcd.message(message)

