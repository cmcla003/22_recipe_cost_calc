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

# yes_no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response= "no"
            return response
        else:
            print("Please enter yes or no")

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


# main routine
# dictionary with conversion values for common units
unit_convert_ml={'tsp': 5, 'tbsp': 15,
           'C': 237,'g':1,'L': 1000 ,'ml': 1}

# scale factor
scale_ok = "no"
while scale_ok =="no":
    serving_size = num_check("How many servings is the recipe? ")
    desired_serving = num_check("How many servings are needed? ")

    scale_factor = desired_serving/serving_size

    if scale_factor < 0.25:
        sf_ok = yes_no("""Warning this scale is small,
accurate measurement of ingredients may be hard.
Do you want to keep going? Yes/No """)
        if sf_ok == "yes":
            break
    elif scale_factor > 4:
        sf_ok = input("""Warning this scale is large,
be aware you have enough space for all ingredients.
Do you want to keep going? Yes/No """)
        if sf_ok == "yes":
            break
    else:
        print("Scale factor: {}".format(scale_factor))

# ingredient, unit and amount
ingredient_list=[]

stop= ""
while stop != "xxx":
    ingredient = not_blank("Please enter the ingredient: ","no")

    if ingredient == "xxx" and len(ingredient_list)>=2:
        break
    elif ingredient == "xxx" and len(ingredient_list)<=1:
        print("Please enter more than 2 ingredients")
    elif ingredient in ingredient_list:
        print("You have already entered this ingredient, Please enter another")
    else:
        amount = num_check("How much? ")
        unit = unit_check()
        converted_amount = convert_to_ml()
        scaled = converted_amount * scale_factor

        # rounding
        if scaled % 1 == 0:
            scaled = round(scaled)
        elif scaled * 10 % 1 == 0:
            scaled ="{:.1f}".format(scaled)
        else:
            scaled = "{:.2f}".format(scaled)

        ingredient_list.append([scaled,unit,ingredient])

print(ingredient_list)
