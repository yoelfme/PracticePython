#!/usr/bin/env python

print("this is a basic string")
print("we learned to join two strings using " + "the plus operation")

print("Including an integer works with %%d like this: %d" % 10)

print("An integer converted to a float with %%f: %f" % 5)

print("A normal float with %%f: %f" % 1.2345)

print("A really large number with %%E: %E" % 6.789E10)

print("Controlling the number of decimal places show: %.02f" % 25.101010101)

print("""The %% behaves differently when combiend with other letters,
like this: %%d %%s %%f %d""" % 10)
