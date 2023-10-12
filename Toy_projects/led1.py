#This is just a test
from gpiozero import LED

led_red = LED(20)

while True:
  led_red.on()
