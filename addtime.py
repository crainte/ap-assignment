#!/usr/bin/env python -B
import re


def add_time(current_time, additional_time):
    # current_time can be "[H]H:MM {AM|PM}"
    # additional_time is number of minutes to add to the time of day
    # return should be same format

    if not isinstance(additional_time, int):
        raise ValueError("Expected Integer as second argument")

    # AM/PM are case sensitive here, not sure if wanted
    if not re.match(r"[0-1]?[0-9]:[0-5][0-9] [A|P]M$", current_time):
        raise SyntaxError("Invalid format. Please use [H]H:MM {AM|PM}")

    # break the string into parts
    time, period = current_time.split()

    # break into hours and minutes
    hour, minute = time.split(":")

    # validate hours
    if int(hour) > 12 or int(hour) < 1:
        raise ValueError("Hours must be between 1-12")

    # find minute sum
    minute_sum = int(minute) + int(additional_time)
    # leftover after mod is the remaining minutes of new time
    m_remainder = minute_sum % 60
    # the quotient should be the additional hours to add on
    add_hours = int(minute_sum//60)
    # zfill the remainder to look pretty
    final_minutes = str(m_remainder).zfill(2)

    # find hour sum
    hour_sum = int(hour) + int(add_hours)
    # this should be the hour of the new time
    h_remainder = hour_sum % 12
    # this should be the amount of toggles required of the time period
    toggles = int(hour_sum//12)

    if h_remainder > 0:
        final_hour = h_remainder
    else:
        # put a ceiling on the possible value of hour
        final_hour = max(1, min(hour_sum, 12))

    # find final period
    if toggles % 2 == 0:
        # If the amount of times a period will toggle is even, it won't change
        # from it's current value
        pass
    else:
        if period == "AM":
            period = "PM"
        elif period == "PM":
            period = "AM"
        else:
            raise ValueError("Something went wrong with period validation")
    final_period = period

    return "{hour}:{minute} {period}".format(hour=final_hour, minute=final_minutes, period=final_period)
