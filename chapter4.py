#!/usr/bin/env python

# Comparing Values for Sameness
print(1 == 1)
print(1 == 2)

print(1.23 == 1)
print(1.0 == 1)

# Comparing strings
a = "Mackintosh apples"
b = "Black Berries"
c = "Golden Delicious apples"

print(a == b)
print(b == c)

print(a[-len("apples"):-1] == c[-len("apples"):-1])

# Comparing list
apples = ["Mackintosh", "Golden Delicious", "Fuji", "Mitsu"]
apple_trees = ["Golden Delicious", "Fuji", "Mitsu", "Mackintosh"]

print(apples == apple_trees)

apple_trees = ["Mackintosh", "Golden Delicious", "Fuji", "Mitsu"]

print(apples == apple_trees)

# Comparing dictionaries
tuesday_breakfast_old = {"pancakes": 10, "french toast": 4, "bagels": 32,
                         "omelets": 12, "eggs and sassuages": 13}

wednesday_breakfast_sold = {"pancakes": 8, "french toast": 5, "bagels": 22,
                            "omelets": 16, "eggs and sausages": 22}

print(tuesday_breakfast_old == wednesday_breakfast_sold)

thursday_breakfast_sold = {"pancakes": 10, "french toast": 4, "bagels": 32,
                           "omelets": 12, "eggs and sassuages": 13}

print(tuesday_breakfast_old == thursday_breakfast_sold)

# Comparing Values for Difference
print(3 != 3)
print(5 != 4)

print(tuesday_breakfast_old != wednesday_breakfast_sold)
print(tuesday_breakfast_old != thursday_breakfast_sold)

# Comparing Greater Than and Less Than
print(5 < 3)
print(10 > 2)

print("a" > "b")
print("A" > "b")
print("A" > "a")
print("b" > "A")
print("Z" > "a")

print("Zebra" > "aardvark")
print("Zebrc" > "Zebrb")
print("Zebra" < "Zebrc")

print("Pumpkin" == "pumpkin")
print("Pumpkin".lower() == "pumpkin".lower())
print("Pumpkin".upper() == "pumpkin".upper())
print("Pumpkin".lower() == "pumpkin")

gourd = "Calabash"
print(gourd.lower())
print(gourd.upper())

# More Than or Equal, Less Than or Equal
print(1 > 1)
print(1 >= 2)
print(10 < 10)
print(10 <= 10)

# Reversing the Outcome of a Test
print(not 5 > 2)
print(not "A" < 3)
print(not "A" < "z")

# Operator AND
print(True and True)
print(False and True)
print(True and False)
print(False and False)

# Operator OR
print(True or True)
print(False or True)
print(True or False)
print(False or False)
