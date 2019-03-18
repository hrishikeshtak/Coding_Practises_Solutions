#!/usr/bin/python3

import time

DAYS = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']

MONTH = ['JAN', 'FEB', 'MAR', 'APR', 'MAY',
         'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
         'NOV', 'DEC']


for _ in range(int(input())):
    epoch_time = time.gmtime(int(input()))
    day = epoch_time.tm_mday
    month = epoch_time.tm_mon
    year = epoch_time.tm_year
    week_day = epoch_time.tm_wday
    if day < 10:
        day = "0{}".format(day)
    print("{}-{}-{} {}".format(day, MONTH[month-1], year, DAYS[week_day]))
