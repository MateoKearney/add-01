from machine import Pin
from time import sleep
led1 = Pin(2, Pin.OUT, value = 0)
led2 = Pin(1, Pin.OUT, value = 0)
btn1 = Pin(28, Pin.IN)
btn2 = Pin(27, Pin.IN)
x = 11

while x == 11:
  if btn1.value() == 1:
    led1.on()
  else:
    led1.off()
    
  if btn2.value() == 1 and led2.value() == 0:
      led2.on()
  elif btn2.value() == 1 and led2.value() == 1:
      led2.off()

  sleep(.5)
