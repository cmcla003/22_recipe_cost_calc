# not blank and checks for digit user entry
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

# number check
def num_check(question):
    error= "Please enter a number more than 0"

    valid = False
    while not valid:
        try:
            response = eval(input(question))

            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

# check unit valid if not leave unchanged
def unit_check():
    unit_to_check = not_blank("Unit: ","no")

    valid_units=[["t", "tsp", "teaspoon", "teaspoons"],
                 ["T", "tbsp", "tablespoon", "tablespoons"],
                 ["C", "c", "cup", "cups"],
                 ["L", "l", "litre", "litres"],
                 ["ml", "mls", "millilitre","millilitres"],
                 ["g","gms","gram","grams"]]

    if unit_to_check in valid_units[0]:
        unit = "tsp"
    elif unit_to_check in valid_units[1]:
        unit = "tbsp"
    elif unit_to_check in valid_units[2]:
        unit = "C"
    elif unit_to_check in valid_units[3]:
        unit = "L"
    elif unit_to_check in valid_units[4]:
        unit = "ml"
    elif unit_to_check in valid_units[5]:
        unit = "g"
    else:
        unit = unit_to_check

    return unit

def convert_to_ml():
    if unit in unit_convert_ml:
        multiply_unit = unit_convert_ml.get(unit)
        converted_amount = amount * multiply_unit

    else:
        converted_amount = amount * 1

    return converted_amount


def general_converter(how_much,lookup,dictionary, conversion_factor):
    if lookup in dictionary:
        multiply_by = dictionary.get(unit)
        how_much = how_much * float(multiply_by) * conversion_factor

    return how_much

# *** main routine ***

# dictionary with conversion values for common units
unit_convert_ml={'tsp': 5, 'tbsp': 15,
           'C': 237,'g':1,'L': 1000 ,'ml': 1}

recipe_unit_amount = []

keep_going = ""
while keep_going != "xxx":

    amount = eval(input("How much? "))
    amount = float(amount)
    unit = unit_check()

    amount = general_converter(amount, unit,unit_convert_ml,1)
    recipe_unit_amount.append([amount,unit])


    print("**{} ml is {} {}".format(recipe_unit_amount,amount,unit))

