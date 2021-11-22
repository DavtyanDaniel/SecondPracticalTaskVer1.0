"""
This is module that collects all constants
"""
from datetime import timedelta

DEC_RANGE = 57
RA_RANGE = 24
SECONDS_IN_27_DAYS = int(timedelta(days=27, hours=7, minutes=12).total_seconds())
SECONDS_IN_14_DAYS = int(timedelta(days=14).total_seconds())
RA_CHANGE_AVERAGE = RA_RANGE / SECONDS_IN_27_DAYS
DEC_CHANGE_AVERAGE = DEC_RANGE / SECONDS_IN_14_DAYS

