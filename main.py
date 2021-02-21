#!/usr/bin/python

import LCD
import sensors
import emailer
import gpio
import thingspeak
import serials
import time
import python_call_shell
import actuadors

if __name__ == "__main__":
  actuadors.initGpio()
  LCD.initialScreen()
  serials.initSerial()
  count = 0
  timeout_door_open = 0
  timeout_send_thingspeak = 0


  while True:
   if count <= 100:
     time.sleep(.01)
     count = count + 1
   else:
     LCD.clear()
     LCD.printMessage("Temp: ")  
     LCD.printMessage(str(sensors.TemperatureGet()))
     if timeout_send_thingspeak > 100:
       timeout_send_thingspeak = 0
       thingspeak.upload(sensors.TemperatureGet())
     serials.write("sendet\n\r")
     timeout_send_thingspeak = timeout_send_thingspeak + 1
     print timeout_send_thingspeak
     count = 0

   read = serials.receiveByte(1)
   if read >= 'A':
      print read
      actuadors.setLamp(read) 
      read = 0



   if(sensors.DoorCheckState()):
     #print "the Door is open"
     timeout_door_open = timeout_door_open + 1
     if timeout_door_open > 1000:
       emailer.alertMe("House Message","The door has been left open for a 10 seconds, maybe is good to check it") 
       timeout_door_open = 0
   else:
     timeout_door_open = 0
    # print "The door is closed"

   if(sensors.WindowCheckState()):
     #print "Window is open"
     #capture a photo
     python_call_shell.capture()
     #send message to email
     emailer.sendAttach("Window Violation", "Check it", "photo.jpeg")
     #remove image
     python_call_shell.remove()
     
   #else:
    # print "Window is closed"

      
