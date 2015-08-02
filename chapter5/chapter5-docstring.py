#!/usr/bin/env python


def in_fridge():
    """This is a function to see if the fridge has a food.
fridge has to be a dictionary defined outside of the function.
the food to be searched for is in the string wanted_food"""
    try:
        count = fridge[wanted_food]
    except Exception:
        count = 0

    return count
