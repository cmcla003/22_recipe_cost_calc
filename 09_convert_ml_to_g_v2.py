import csv
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

def general_converter(how_much, lookup,dictionary,conversion_factor):

    if lookup in dictionary:
        multiply_unit = dictionary.get(unit)
        how_much = how_much * multiply_unit * conversion_factor

    return how_much

# main routine

# dictionary for ml to g ingredients
# open file, read data into list convert to dictionary
groceries = open('01_ingredients_ml_to_g.csv')
csv_groceries = csv.reader(groceries)
food_dict={}
for row in csv_groceries:
    food_dict[row[0]] = row[1]

# dictionary with conversion values for common units
unit_convert_ml={'tsp': 5, 'tbsp': 15,
           'C': 237,'g':1,'L': 1000 ,'ml': 1}

keep_going=""
while keep_going =="":
    ingredient = input("Ingredient: ").lower().strip()

    amount=eval(input("How much: "))
    amount = float(amount)
    # check unit valid
    unit = unit_check()
    # convert unit to ml
    amount = general_converter(amount, unit, unit_convert_ml,1)
    print("{} ml".format(amount))
    #convert unit from ml to g
    ingredient = general_converter(amount,ml, food_dict,250)
    print("{} g".format(ingredient))




