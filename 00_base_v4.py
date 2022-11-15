# imports
import re

# *** functions and methods ***
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

# yes_no checker
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

# number check valid number
def num_check(question):
    error= "Please enter a number"

    valid = False
    while not valid:
        try:
            response = eval(input(question))

            if response < 0:
                print(error)
            else:
                return response
        except (NameError,ValueError,SyntaxError):
            print(error)

# scale serving based on user needs
def scale_servings():
    scale_ok = "no"
    while scale_ok =="no":
        serving_size = num_check("How many servings is the recipe? ")
        desired_serving = num_check("How many servings are needed? ")

        scale_factor = desired_serving/serving_size

        if scale_factor < 0.25:
            sf_ok = input("""Warning this scale is small,
    accurate measurement of ingredients may be hard.
    Do you want to keep going? Yes/No """).strip().lower()
            if sf_ok == "yes" or sf_ok == "y":
                scale_ok ="yes"

        elif scale_factor > 4:
            sf_ok = input("""Warning this scale is large,
    be aware you have enough space for all ingredients.
    Do you want to keep going? Yes/No """).strip().lower()
            if sf_ok == "yes" or sf_ok == "y":
                scale_ok ="yes"
        else:
            scale_ok = "y"
    return scale_factor

# ask user for amount, unit, ingredient
def get_all_ingredients():
    duplicate_error = "You have already entered this ingredient, Please enter another"
    all_ingredients =[]
    stop = ""
    print("Please enter ingredients one line at a time. Press 'xxx' when finished")

    while stop != "xxx":
        get_recipe_line = not_blank("Recipe Line: ","yes").lower()

        if get_recipe_line == "xxx" and len(all_ingredients)>= 2:
            break
        elif get_recipe_line == "xxx" and len(all_ingredients)< 2:
            print("You need at least 2 ingredients, please add more.")

        else:
            all_ingredients.append(get_recipe_line)

    return all_ingredients

# *** Main Routine ***
# initalise lists

# ask user recipe name and source
recipe_name = not_blank("What is the name of your recipe? ","no")
recipe_source = not_blank("Where did you get your recipe from? ","yes")

# ask for recipe servings and desired servings
scale_factor = scale_servings()
# print for testing
print("Scale factor: {:.2f}".format(scale_factor))

# get amount unit and ingredient from user
full_recipe = get_all_ingredients()
# print testing recipe list
print(full_recipe)

# split out amount, unit, ingredient
for recipe_line in full_recipe:
    convert = "yes"
    mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

    if re.match(mixed_regex,recipe_line):

        # get mixed number by matching to regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()
        # change amount to a decimal
        amount= mixed_num.replace(" ","+")
        amount = eval(amount)
        # get unit and ingredient
        compile_regex = re.compile(mixed_regex)
        unit_ingredient = re.split(compile_regex,recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip()

    else:
        # allows for units is pinch/dash
        get_amount = recipe_line.split(" ", 1)
        try:
            amount = eval(get_amount[0])
        except NameError:
            amount = get_amount[0]
            convert="no"

        unit_ingredient = get_amount[1]

    get_unit = unit_ingredient.split(" ", 1)

    # get uni and ingredient name
    unit= get_unit[0]
    ingredient = get_unit[1]

    # print for testing
    print("*{}* {} {}".format (amount, unit, ingredient))
