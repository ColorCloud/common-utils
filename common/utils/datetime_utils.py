# -*- coding: utf-8 -*-
'''
Created on 2017-03-20

@author: lishiwei
'''
from datetime import datetime, date, timedelta
from .errors import raise_error


def drange(start, stop, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    """Datetime range, like python built-in range function

    params:
        start       : start datetime
        stop        : stop datetime
        days        : days steps
        seconds     : seconds steps
        microseconds: microseconds steps
        milliseconds: milliseconds steps
        minutes     : minutes steps
        hours       : hours steps
        weeks       : weeks steps

    returns: one iterator
    """
    if not isinstance(start, (datetime, date)) or not isinstance(stop, (datetime, date)):
        raise_error(TypeError("bad type for start or stop, neither datetime nor date"))

    delta = timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)
    if delta.total_seconds() == 0:
        raise_error(
            ValueError("bad value for steps(days, seconds, microseconds, milliseconds, minutes, hours, weeks)"))

    value = datetime(start.year, start.month, start.day) if type(start) == date else start
    stop = datetime(stop.year, stop.month, stop.day) if type(stop) == date else stop
    if delta.total_seconds() > 0:
        while value < stop:
            yield value
            value += delta
    else:
        while value > stop:
            yield value
            value += delta
