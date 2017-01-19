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
upper_frame_corner = (0, 0)
lower_frame_corner = (7, 7)
highest_value = 7
off = (0, 0, 0)

hat.clear()
hat.rotation(270)
hat.brightness(0.3)

def display_binary(value, row, color):
	binary_str = "{0:8b}".format(value)
	for x in range(0, 8):
		if binary_str[x] == '1':
			hat.set_pixel(x - 2, row, color[0], color[1], color[2])
		else:
			hat.set_pixel(x - 2, row, 0, 0, 0)	

def display_frame():
	if upper_frame_corner[0] < highest_value:
		upper_frame_corner = (upper_frame_corner[0] + 1, upper_frame_corner[1])

	hat.set_pixel(upper_frame_corner[0], upper_frame_corner[1], frame_color[0], frame_color[1], frame_color[2])

while True:
    t = datetime.datetime.now()
    tens_hour = t.hour // 10
    ones_hour = t.hour % 10
    tens_minute = t.minute // 10
    ones_minute = t.minute % 10
    tens_second = t.second // 10
    ones_second = t.second % 10
    # display_binary(t.year % 100, 0, year_color)
    # display_binary(t.month, 1, month_color)
    # display_binary(t.day, 2, day_color)
    display_binary(tens_hour, 6, hour_color)
    display_binary(ones_hour, 5, hour_color)
    display_binary(tens_minute, 4, minute_color)
    display_binary(ones_minute, 3, minute_color)
    display_binary(tens_second, 2, second_color)
    display_binary(ones_second, 1, second_color)
    # display_binary(t.microsecond / 10000, 0, hundredths_color)
    # display_frame()
    hat.show()
    time.sleep(1)
    # time.sleep(0.0001)
