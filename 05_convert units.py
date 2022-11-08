# not blank function
def not_blank(question,number_ok):
    error = "Cannot be blank"
    digi_error = "Cannot have numbers"
    valid = False
    while not valid:
        # ask user for entry and assesses if not blank
        response = input(question).strip().lower()
        has_errors = ""

        if number_ok != "yes":
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        if has_errors != "":
            print(digi_error)
        else:
            return response
            valid = True


# dictionary with conversion values for common units
unit_dict={'kg': 1000, 'pound':450, 'ounce':30, 'grams':1,
                'teaspoon': 4.92, 'tablespoon': 14.7,
                'cup': 128,
                'litre': 1000, 'quart':946.35, 'pint':473.17 ,'ml': 1}

# list of abbreviations
valid_units = [["kg","kilo","kilogram"],["lb","lbs", "pound"],["oz","ounce"],
               ["g", "gm", "grams"],["t", "tsp", "teaspoon"],["T","tbsp","tablespoon",],
               ["C","c","cup"],["l", "L", "litre"],["qt","quart"],["pt","pint"],["mls", "millilitre","ml"]]

recipe_units = []

unit = ""
while unit != "xxx":

    unit = not_blank("Please enter a unit of measurement: ","no")

    if unit == "xxx":
        break
    else:
        recipe_units.append(unit)



print(recipe_units)





