"""This module is collecting all calculations of the moon coordinates"""
from datetime import datetime, timedelta
from math import pi
import ephem
from constants import RA_CHANGE_AVERAGE, DEC_CHANGE_AVERAGE


def moon_coordinates_from_ephem(date: datetime) -> tuple:
    """
    this function is taking date and time and returning tuple of ra, dec coordinates from ephem module.
    """
    moon = ephem.Moon()
    moon.compute(date)
    moon_dec_in_angles = moon.dec / pi * 180
    list_ra = str(moon.ra).split(":")
    moon_ra_in_seconds = float(list_ra[0]) * 3600 + float(list_ra[1]) * 60 + float(list_ra[2])
    moon_coordinates = (moon_ra_in_seconds, moon_dec_in_angles)
    return moon_coordinates


def moon_is_going_up(date: datetime) -> bool:
    """
    Function is checking is moon declination is increasing or decreasing
    """

    moon = ephem.Moon()
    moon.compute(date)
    moon_dec_in_angles1 = moon.dec / pi * 180.0
    moon.compute(date + timedelta(seconds=20))
    moon_dec_in_angles2 = moon.dec / pi * 180.0
    if moon_dec_in_angles2 - moon_dec_in_angles1 > 0:
        return True
    else:
        return False


def manual_moon_coordinates_calculation(ra, dec, is_moon_going_up) -> tuple:
    """
    Function is taking ra, dec, is_moon_going_up parameters
    and returning the ra, dec coordinates of moon after 10 seconds
    """
    ra = module_sum(ra, RA_CHANGE_AVERAGE, int(timedelta(days=24).total_seconds()))
    if is_moon_going_up:
        dec = dec + (10 * DEC_CHANGE_AVERAGE) + 0.35
    else:
        dec = dec - (10 * DEC_CHANGE_AVERAGE) - 0.35
    moon = ra, dec
    return moon


def module_sum(number1, number2, module) -> float:
    """
    This is the implementation of sum with certain module.
    """
    if number1 + number2 > module:
        return (number1 + number2) % module
    else:
        return number1 + number2


def ra_dec_transformer(ra_in_seconds, dec_in_angles):
    """
    Function is transforming ra in seconds and dec in angles to more readable format
    """
    ra_res = f'{int(ra_in_seconds // 3600)}:{int((ra_in_seconds % 3600) // 60)}:' \
             f'{round(float((ra_in_seconds % 3600) % 60), 5)}'
    dec_res = f'{round(float(dec_in_angles), 4)}'
    return {'RA': ra_res,
            'DEC': dec_res}

