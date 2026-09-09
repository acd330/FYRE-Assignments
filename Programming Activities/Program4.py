# Blinking program- green LED 

# import modules
import machine     #module w microcontroller stuff
import time        #module w time methods

# make led object- green LED is gpio pin 0
led = machine.Pin(0, machine.Pin.OUT)

# infinite loop
while True:
  led.value(1)     #turn on LED
  time.sleep(.25)  #.25 sec delay
  led.value(0)     #turn off LED
  time.sleep(.25)  #delay again