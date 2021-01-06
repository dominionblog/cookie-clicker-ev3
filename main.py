#!/usr/bin/env python3
from ev3dev2.display import Display
from ev3dev2.button import Button
import ev3dev2.fonts as fonts
from ev3dev2.sensor.lego import TouchSensor

screen = Display()
button = Button()
ts = TouchSensor()

count = 0
waiting_release = False

while True:
    screen.clear()
    screen.text_pixels("How many times you've", x=3, y=0,
                       clear_screen=False, 
                       font=fonts.load('courB12'))
    screen.text_pixels("pressed it: ", x=3, y=10, clear_screen=False, font=fonts.load('courB12'))
    screen.text_pixels(str(count), x=3, y=70, clear_screen=False, font=fonts.load('lubB24'))
    screen.update()
    if ts.is_pressed and (not waiting_release):
        count += 1
        waiting_release = not waiting_release
    if ts.is_released and waiting_release:
        waiting_release = not waiting_release
