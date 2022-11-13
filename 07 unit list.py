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

keep_going =""
while keep_going =="":
    recipe_unit = []

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

    recipe_unit.append(unit)
    print(recipe_unit)







