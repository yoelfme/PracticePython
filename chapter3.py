#!/usr/bin/env python

first_string = "This is a string"
second_string = "This is a another string"
first_number = 4
second_number = 5
print("The fisrt variables are %s, %s, %d, %d" % (
    first_string, second_string, first_number, second_number))

first_string2 = 245
second_number2 = "This isn't a number"

print(first_string2)
print(second_number2)

proverb = "A penny saved"
proverb = proverb + " is a penny earned"

print(proverb)

pennies_saved = 0
pennies_saved = pennies_saved + 1

print(pennies_saved)

pennies_saved = 1
pennies_earned = pennies_saved

print(pennies_earned)

pennies_saved = pennies_saved + 1

print(pennies_saved)

print("A %s %s %s %s" % ("string", "filled", "by a", "tuple"))

# Tuples
filler = ("string", "filled", "by a", "tuple")
print("A %s %s %s %s" % filler)

print(filler)

a = ("first", "second", "third")
print("The fisrt element of the tuple is %s" % a[0])
print("The second element of the tuple is %s" % a[1])
print("The third element of the tuple is %s" % a[2])

print("Lenght of tuple: %d" % len(a))
print(a[len(a) - 1])

b = (a, "b is second element")
print(b)

print("%s" % b[1])
print("%s" % b[0][0])
print("%s" % b[0][1])
print("%s" % b[0][2])

layer2 = b[0]

print(layer2[0])
print(layer2[1])
print(layer2[2])

single_element_tuple = ("the sole element",)

print(type(single_element_tuple))

# Lists
breakfast = ["coffee", "tea", "toast", "egg"]

count = 0
print("Today's breakfast is %s" % breakfast[count])

count = 1
print("Today's breakfast is %s" % breakfast[count])

count = 2
print("Today's breakfast is %s" % breakfast[count])

count = 3
breakfast[count] = "sausages"
print("Today's breakfast is %s" % breakfast[count])

breakfast.append("waffles")
count = 4
print("Today's breakfast is %s" % breakfast[count])

breakfast.extend(["juice", "decaf", "oatmeal"])
print(breakfast)
