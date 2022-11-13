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

def unit_checker():
    unit_check = input("Unit? ")

    valid_units=[["t", "tsp", "teaspoon", "teaspoons"],
                 ["T", "tbsp", "tablespoon", "tablespoons"],
                 ["C", "c", "cup", "cups"],
                 ["L", "l", "litre", "litres"],
                 ["ml", "mls", "millilitre","millilitres"],
                 ["g","gms","gram","grams"]]

    if unit_check in valid_units:
        print("You chose {}".format(valid_units))
    else:
        print("You chose {}, not in valid units".format(unit_check))

# dictionary with conversion values for common units
unit_convert_ml={'teaspoon': 5, 'tablespoon': 15,
           'cup': 237,'gram':1,'litre': 1000 ,'ml': 1}

valid = False
while not valid:
    amount = eval(input("How much? "))
    amount = float(amount)

    unit = unit_checker()
    if unit in unit_convert_ml:
        multiply_unit = unit_convert_ml(unit)
        amount = amount * multiply_unit
        print("Amount in ml {}".format(amount))

    else:
        print("{} is unchanged".format(unit))
