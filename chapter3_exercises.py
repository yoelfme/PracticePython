#!/usr/bin/env python

'''
Create a list called dairy_section with four elements
from the dairy section of a supermarket
'''
dairy_section = ["milk", "yogurt", "cheese", "skim milk"]
print(dairy_section)

'''
Print a string with the first and last elements of the dairy_section list.
'''
join_first_last = dairy_section[0] + " " + dairy_section[-1]
print("%s" % join_first_last)

'''
Create a tuple called milk_expiration with three elements:
the month, day, and year of the
expiration date on the nearest carton of milk.
'''
milk_expiration = ("07", "18", "2015")
print(milk_expiration)

'''
Print the values in the milk_expiration tuple in a string that reads
This milk carton will expire on 12/10/2009.
'''
print("This milk carton will expire on %s/%s/%s" % milk_expiration)

'''
Create an empty dictionary called milk_carton .
Add the following key\/value pairs. You can
make up the values or use a real milk carton
- expiration_date : Set it to the milk_expiration tuple.
- fl_oz : Set it to the size of the milk carton on which you are basing this.
- cost : Set this to the cost of the carton of milk.
- brand_name : Set this to the name of the brand of milk you're using.
'''
milk_carton = {}
milk_carton["expiration_date"] = milk_expiration
milk_carton["fl_oz"] = 12
milk_carton["cost"] = 25.00
milk_carton["brand_name"] = "Delactomy"
print(milk_carton)

'''
Print out the values of all of the elements of the milk_carton
using the values in the dictionary,
and not, for instance, using the data in the milk_expiration tuple
'''
print("Expiration Date: %s/%s/%s" % milk_carton["expiration_date"])
print("Fl Oz: %d" % milk_carton["fl_oz"])
print("Cost: %.02f" % milk_carton["cost"])
print("Brand Name: %s" % milk_carton["brand_name"])

'''
Show how to calculate the cost of six cartons of milk
based on the cost of milk_carton .
'''
cartons = 6
total = cartons * milk_carton["cost"]
print("The total is %.02f" % total)

'''
Create a list called cheeses. List all of the cheeses you can think of.
Append this list to the dairy_section list,
and look at the contents of dairy_section.
Then remove the list of cheeses from the array
'''
cheeses = ["oaxaca", "quesillo", "mantequilla", "provolone"]
dairy_section.append(cheeses)
print(dairy_section)

dairy_section.remove(cheeses)
print(dairy_section)

'''
How do you count the number of cheeses in the cheese list
'''
print("The number of cheeses is %d" % len(cheeses))

'''
Print out the first five letters of the name of your first cheese.
'''
print("%s" % cheeses[0][0:5])
print("%s" % cheeses[1][0:5])
print("%s" % cheeses[2][0:5])
print("%s" % cheeses[3][0:5])
