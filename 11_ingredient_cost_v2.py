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

# check unit valid if not leave unchanged
def unit_check():
    unit_to_check = not_blank("Unit: ","no").strip()

    valid_units=[["t", "tsp", "teaspoon", "teaspoons"],
                 ["T", "tbsp", "tablespoon", "tablespoons"],
                 ["C", "c", "cup", "cups"],
                 ["L", "l", "litre", "litres"],
                 ["ml", "mls", "millilitre","millilitres"],
                 ["g","gms","gram","grams"],
                 ["kg","kgs","kilograms","kilogram"]]

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
    elif unit_to_check in valid_units[6]:
        unit = "kg"
    else:
        unit = unit_to_check

    return unit


# dictionary with conversion values for common units
unit_convert_ml={'tsp': 5, 'tbsp': 15,
           'C': 237,'g':1,'L': 1000 ,'ml': 1,'kg':1000}

calculated_ml_g =[]

keep_going =""
while keep_going =="":
    ingredient = input("Ingredient: ")
    if ingredient == "xxx":
        break
    cost = float(input("How much does it cost? "))
    amount = float(input("Purchase size: "))
    unit = unit_check()

    # convert unit to ml/g for cost
    if unit in unit_convert_ml:
        multiply_unit = unit_convert_ml.get(unit)
        amount = amount * multiply_unit

    else:
        amount = amount * 1

    # calculate unit cost
    ingredient_amount_per_unit = cost / amount

    calculated_ml_g.append([amount,ingredient_amount_per_unit])

print(calculated_ml_g)


