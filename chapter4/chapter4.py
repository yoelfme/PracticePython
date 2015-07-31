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

# How to Get Decisions Made
if 1 > 2:
    print("No it is not!")

if 2 > 1:
    print("Yes it is!")

# Placing Tests within Tests
omelet_ingredients = {"egg": 2, "mushroom": 5, "pepper": 1,
                      "cheese": 1, "milk": 1}

fridge_contents = {"egg": 10, "mushroom": 20, "pepper": 3,
                   "cheese": 2, "tomato": 4, "milk": 15}

have_ingredients = [False]

if fridge_contents["egg"] > omelet_ingredients["egg"]:
    have_ingredients[0] = True
    have_ingredients.append("egg")

print(have_ingredients)

if fridge_contents["mushroom"] > omelet_ingredients["mushroom"]:
    if have_ingredients[0] is False:
        have_ingredients[0] = True
    have_ingredients.append("mushroom")

print(have_ingredients)

# if... elif statements
milk_price = 1.50

if milk_price < 1.25:
    print("Buy two cartons of milk , they're on sale")
elif milk_price < 2.00:
    print("Buy one carton of milk, prices are normal")
elif milk_price > 2.00:
    print("Go somewhere else! Milk costs too much here")

# if... elif...  else statement
OJ_price = 2.50
if OJ_price < 1.25:
    print("Get one, I'm thirsty")
elif OJ_price <= 2.00:
    print("Ummm... sure, but I'll drink it slowly")
else:
    print("I do not have enough money. Never mind")

# Using a while Loop
i = 10
while i > 0:
    print("Lift off in: %d" % i)
    i = i - 1

# Using a for Loop
for i in range(10, 0, -1):
    print("T-minus: %d" % i)

for i in range(10):
    print(i)

# infinite loop

'''
while True:
    print("You're going to get bored with this quickly")
'''

'''
test a possible infinite loop
for Python 2.7 use the function raw_input
for Python 3.x use the function input
'''
age = 0
while True:
    how_old = raw_input("Enter your age: ")
    if how_old == "No":
        print("Don't be ashamed of your age!")
        break
    num = int(how_old)
    age = age + num
    print("Your age is %d" % age)
    print("That is old!")

# Using else While Repeating
for food in ("pate", "cheese", "crackers", "yogurt"):
    if food == "yogurt":
        break
else:
    print("There is no yogurt")

for food in ("pate", "cheese", "crackers"):
    if food == "yogurt":
        break
else:
    print("There is no yogurt")

# Using continue to Keep Repeating
for food in ("pate", "cheese", "rotten apples",
             "crackers", "whip cream", "tomato soup"):
    if food[0:6] == "rotten":
        continue

    print("Hey, you can eat %s" % food)

# Handling Errors
fridge_contents = {"egg": 10, "mushroom": 20, "pepper": 3,
                   "cheese": 2, "tomato": 4, "milk": 15}

try:
    if fridge_contents["orange juice"] > 3:
        print("Sure, let's have some juice")
except KeyError:
    print("Awww, there is no juice. Let's go shopping!")

# Creating an Exception with Its Explanation
try:
    if fridge_contents["orange juice"] > 3:
        print("Sure, let's have some juice")
except (KeyError) as error:
    print("Woah! There is no %s" % error)

# Set tuple  with some exception types

try:
    if fridge_contents["orange juice"] > 3:
        print("Sure, let's have some juice")
except (KeyError, TypeError) as error:
    print("Woah! There is no %s" % error)

# Pass exception
try:
    if fridge_contents["orange juice"] > 3:
        print("Sure, let's have some juice")
except (KeyError) as error:
    print("Woah! There is no %s" % error)
except (TypeError):
    pass
else:
    print("All is well")
