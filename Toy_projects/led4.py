from gpiozero import LED
from time import sleep

led = {
    "red" : LED(17),
    "yellow" : LED(27),
    "green" : LED(22)

}

while True:
    for i in led.keys():
        led[i].blink(on_time=1, off_time=1)
        sleep(2)