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


# Ditionaries
menus_specials = {}
menus_specials["breakfast"] = "Canadian ham"
menus_specials["lunch"] = "tuna surprise"
menus_specials["dinner"] = "cheeseburge deluxe"

print(menus_specials)

menus_specials = {"breakfast": "sausage and eggs",
                  "lunch": "split pea soup and garlic bread",
                  "dinner": "2 hot dogs and onion rings"}

print(menus_specials)
print("%s" % menus_specials["breakfast"])
print("%s" % menus_specials["lunch"])
print("%s" % menus_specials["dinner"])

hungry = menus_specials.keys()
print(list(hungry))

starving = menus_specials.values()
print(list(starving))

menu = {"breakfast": "spam", "lunch": "spam",
        "dinner": "Spam with a side of spam"}

print(menu)
print(menu.get("lunch"))
print(menu.get("breakfast"))

menu2 = {"breakfast": "spam", "breakfast": "ham",
         "dinner": "Spam with a side of spam"}

print(menu2.get("breakfast"))

# Treating a string like a list
last_names = ["Douglas", "Jefferson", "Williams", "Frank", "Thomas"]
print("%s" % last_names[0])
print("%s" % last_names[0][0])

print("%s" % last_names[1])
print("%s" % last_names[1][0])

print("%s" % last_names[2])
print("%s" % last_names[2][0])

print("%s" % last_names[3])
print("%s" % last_names[3][0])

print("%s" % last_names[4])
print("%s" % last_names[4][0])

by_letter = {}
by_letter[last_names[0][0]] = last_names[0]
by_letter[last_names[1][0]] = last_names[1]
by_letter[last_names[2][0]] = last_names[2]
by_letter[last_names[3][0]] = last_names[3]
by_letter[last_names[4][0]] = last_names[4]

print(by_letter)

# None, True o False
print(True)
print(False)
print(True == 1)
print(True == 0)
print(False == 1)
print(False == 0)
print(False > 0)
print(False < 1)

# Referencing the last elements
last_element = len(last_names) - 1
print('%s' % last_names[last_element])
print('%s' % last_names[-1])

# Slicing sequences
slice_me = ("The", "next", "time", "we", "meet", "drinks", "are", "on", "me")
sliced_tuple = slice_me[5:9]
print(sliced_tuple)

slice_this_list = ["The", "next", "time", "we", "meet", "drinks",
                   "are", "on", "me"]

sliced_list = slice_this_list[5:9]
print(sliced_list)

slice_this_string = "The next time we meet drinks are on me"
sliced_string = slice_this_string[5:9]
print(sliced_string)

# Growing Lists by Appending Sequences
living_room = ("rug", "table", "chair", "TV", "dustbin", "shelf")
apartment = []
apartment.extend(living_room)
print(apartment)

# Popping Elements from a List
todays_temperatures = [23, 32, 33, 31]
todays_temperatures.append(29)
print(todays_temperatures)

morning = todays_temperatures.pop(0)
print('This mornings temperature was %.02f' % morning)

late_morning = todays_temperatures.pop(0)
print('Todays late morning temperature was %.02f' % late_morning)

noon = todays_temperatures.pop(0)
print('Todays noon temperature was %.02f' % noon)

print('Afternoon temperature was %.02f' % todays_temperatures.pop(0))

print(todays_temperatures)

# Working with sets
alphabet = ['a', 'b', 'b', 'c', 'a', 'd', 'e']
print(type(alphabet))
print(alphabet)

alph2 = set(alphabet)
print(type(alph2))
print(alph2)
