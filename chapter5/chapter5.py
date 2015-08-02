#!/usr/bin/env python


def in_fridge():
    try:
        count = fridge[wanted_food]
    except Exception:
        count = 0
    return count
