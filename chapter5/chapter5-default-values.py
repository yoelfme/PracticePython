#!/usr/bin/env python

def get_omelet_ingredients(omelet_name):
    """This contains a dictionay of omelet names that can be produced,
    and their ingredients"""
    # All of our omeletes need eggs and milk
    ingredients = {"eggs": 2, "milk": 1}
    if omelet_name == "cheese":
        ingredients["cheddar"] = 2
    elif omelet_name == "western":
        ingredients["jak_cheese"] = 2
        ingredients["ham"] = 1
        ingredients["pepper"] = 1
        ingredients["onion"] = 1
    elif omelet_name == "greek":
        ingredients["feta_cheese"] = 2
        ingredients["spinach"] = 2
    else:
        print("That's not on the menu, sorry!")
        return None

    return ingredients


def make_food(ingredients_needed, food_name):
    """make_food(ingredients_needed, food_name)
    Takes the ingredients from ingredients_needed and makes food_name"""
    for ingredient in ingredients_needed.keys():
        print("Adding %d of %s to make a %s" % (ingredients_needed[ingredient],
                                                ingredient,
                                                food_name))

    print("Made %s" % food_name)
    return food_name


def make_omelet(omelet_type = "cheese"):
    """This will make an omelet. You can either pass in a dictionary
    that contains all of the ingredients for your omelet, or provide
    a string to select a type of omelet this function already knows
    about"""
    if type(omelet_type) == type({}):
        print("omelet_type is a dictionary with ingredients")
        return make_food(omelet_type, "Omelet")
    elif type(omelet_type) == type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        print("I don't think I can make this kind of omelet: %s" % omelet_type)
