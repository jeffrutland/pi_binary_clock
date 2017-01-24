#!/usr/bin/env python

import unicornhat as hat
import time, datetime

year_color = (0, 255, 0)
month_color = (0, 0, 255)
day_color = (255, 0, 0)
hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
hundredths_color = (127, 127, 0)
frame_color = (200, 200, 200)
frame_index = 0 # starting index
highest_value = 7
off = (0, 0, 0)

hat.clear()
hat.rotation(270)
hat.brightness(0.3)

def display_binary(value, row, color):
    binary_str = "{0:8b}".format(value)
    # print value
    print binary_str
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, color[0], color[1], color[2])
        else:
            hat.set_pixel(x, row, 0, 0, 0)  

def display_frame():
    # side...
    hat.set_pixel(0, frame_index, frame_color[0], frame_color[1], frame_color[2])
    # hat.set_pixel(frame_index, 0, frame_color[0], frame_color[1], frame_color[2])
    # hat.set_pixel(7, frame_index, frame_color[0], frame_color[1], frame_color[2])
    # hat.set_pixel(frame_index, 7, frame_color[0], frame_color[1], frame_color[2])


def advance_index():
        global frame_index
        # print frame_index
        if frame_index < highest_value:
                frame_index = frame_index + 1
        else:
                frame_index = 0

while True:
    t = datetime.datetime.now()
    # attempt to 12 hours using modulus
    temp_hour = t.hour % 12
    # split values into seperate digits for hour
    tens_hour = (temp_hour // 10)
    ones_hour = (temp_hour % 10)
    # split values into seperate digits for minute
    tens_minute = (t.minute // 10)
    ones_minute = (t.minute % 10)
    # split values into seperate digits for second
    tens_second = (t.second // 10)
    ones_second = (t.second % 10)
    # bit-shift everything to the left 2 spaces to center the display
    display_binary(tens_hour << 2, 6, hour_color)
    display_binary(ones_hour << 2, 5, hour_color)
    display_binary(tens_minute << 2, 4, minute_color)
    display_binary(ones_minute << 2, 3, minute_color)
    display_binary(tens_second << 2, 2, second_color)
    display_binary(ones_second << 2, 1, second_color)
    advance_index()
    hat.show()
    time.sleep(1)
    # time.sleep(0.0001)
