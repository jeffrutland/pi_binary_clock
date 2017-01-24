#!/usr/bin/env python

import unicornhat as hat
import time, datetime

hour_color = (0, 175, 125)
minute_color = (0, 0, 175)
second_color = (125, 0, 175)
hundredths_color = (127, 127, 0)
frame_color = (90, 90, 90)
shift_index = 0 # starting index
highest_value = 7
off = (0, 0, 0)

hat.clear()
hat.rotation(180)
hat.brightness(0.5)

def display_binary(value, row, color):
    # determine the color to use... if none, use frame color
    if color is None:
            draw_color = frame_color
    else:
            draw_color = color

    # add a value here to animate on the time rows
    # if shift_index == row:
        # value = value + 128
        # value = value + 1

    binary_str = "{0:8b}".format(value)
    # print value
    # print binary_str
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, draw_color[0], draw_color[1], draw_color[2])
        else:
            hat.set_pixel(x, row, 0, 0, 0)  

def advance_index():
        global shift_index
        # print shift_index
        if shift_index < highest_value:
                shift_index = shift_index + 1
        else:
                shift_index = 0

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

    # display on the two outer vertical rows
    # display_binary((128 >> shift_index), 7, None)
    # display_binary(1 << shift_index, 0, None)
    
    # bit-shift everything to the left 2 spaces to center the display
    # also, figure out if a value is needed to be added to each here
    # to animate the horizontal rows
    
    # display_binary((tens_hour << 2), 6, hour_color)
    # display_binary((ones_hour << 2), 5, hour_color)
    # display_binary((tens_minute << 2), 4, minute_color)
    # display_binary((ones_minute << 2), 3, minute_color)
    # display_binary((tens_second << 2), 2, second_color)
    # display_binary((ones_second << 2), 1, second_color)

    display_binary(tens_hour, 6, hour_color)
    display_binary(ones_hour, 5, hour_color)
    display_binary(tens_minute, 4, minute_color)
    display_binary(ones_minute, 3, minute_color)
    display_binary(tens_second, 2, second_color)
    display_binary(ones_second, 1, second_color)

    # print 128 >> shift_index
    # print shift_index >> 1

    advance_index()
    hat.show()
    time.sleep(0.1)
