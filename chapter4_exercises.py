#!/usr/bin/env python
'''
Using a series of if ... : statements, evaluate whether the numbers
from 0 through 4 are True or False by creating five separate tests
'''
if 0 is True:
    print("0 is True")

if 1 is True:
    print("1 is True")

if 2 is True:
    print("2 is True")

if 3 is True:
    print("3 is True")

if 4 is True:
    print("4 is True")

if 5 is True:
    print("5 is True")

'''
Create a test using a single if ... : statement that will tell you whether
a value is between 0 and 9 inclusively (that is, the number can be 0 or 9 as
well as all of the numbers in between, not just 1 to 8) and print a message
if it is a success. Test it.
'''
number = 8

if number >= 0 and number <= 9:
    print("The number is between 0 and 9")

'''
Using if ... : , elif , ...: and else: , create a test for whether a value
referred to by a name is in the first two elements of a sequence.
Use the if ... : to test for the first element of the list; use elif ... : to
test the second value referenced in the sequence; and use the else: clause to
print a message indicating whether the element being searched for is not in
the list.
'''
list = ["jhon", "doe", "peter"]
name = "doe"

if name == list[0]:
    print("The name is the first element of list")
elif name == list[1]:
    print("The name is the second element of list")
else:
    print("The name doesn't exists in the list")

'''
Create a dictionary containing foods in an imaginary refrigerator, using the
name fridge . The name of the food will be the key, and the corresponding value
of each food item should be a string that describes the food. Then create a name
that refers to a string containing the name of a food. Call the name
food_sought. Modify the test from Exercise 3 to be a simple if ... : test
(no elif ... : or else: will be needed here) for each key and value in the
refrigerator using a for ... in ... : loop to test every key contained in the
fridge. If a match is found, print a message that contains the key and the value
and then use break to leave the loop. Use an else ... : statement at the end of
the for loop to print a message for cases in which the element wasn't found.
'''
fridge = {
    "cheese": "For the sandwiches",
    "sausage": "For the hot dog",
    "apple": "For the postre"
}
food_sought = "cheese"

for food in fridge:
    if food == food_sought:
        print("The %s is %s" % (food, fridge[food].lower()))
        break
else:
    print("The food wasn't found")

'''
Modify Exercise 3 to use a while ... : loop by creating a separate list called
fridge_list that will contain the values given by fridge.keys . As well,
use a variable named, current_key that will refer to the value of the current
element in the loop that will be obtained by the method fridge_list.pop.
Remember to place fridge_list.pop as the last line of the while... : loop so
that the repetition will end normally. Use the same else: statement at the
end of the while loop as the one used at the end of Exercise 3.
'''
fridge_list = fridge.keys()
current_key = fridge_list.pop()

while len(fridge_list) >= 0:
    if current_key == food_sought:
        print("The %s is %s" % (current_key, fridge[current_key].lower()))
        break
    current_key = fridge_list.pop()
else:
    print("The food wasn't found")

'''
Query the fridge dictionary created in Exercise 3 for a key that is not
present, and elicit an error. In cases like this, the KeyError can be used
as a shortcut to determining whether or not the value you want is in the
list. Modify the solution to Exercise 3 so that instead of using a for ...
in ... : a try: block is used.
'''
food_sought = "hamburger"
try:
    print("The %s is %s" % (food_sought, fridge[food_sought].lower()))
except (KeyError) as e:
    print("The food wasn't found")
