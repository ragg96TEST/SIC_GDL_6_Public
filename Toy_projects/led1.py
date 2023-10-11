from gpiozero import LED

led_red = LED(17)

while True:
  led_red.on()
