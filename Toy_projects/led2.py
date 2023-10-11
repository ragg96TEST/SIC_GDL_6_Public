from gpiozero import LED
from signal import pause

led_red = LED(17)

led_red.blink(1)
pause()
