# imports

# functions & methods
# check input is not blank/ has digits
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

# main routine
#initalise lists
ingredient_list=[]
# ask user recipe name and source
recipe_name = not_blank("What is the name of your recipe? ","no")
recipe_source = not_blank("Where did you get your recipe from? ","yes")

# ask user amount of serving and desired serve scale accordingly
scale_ok = "no"
while scale_ok =="no":
    serving_size = num_check("How many servings is the recipe? ")
    desired_serving = num_check("How many servings are needed? ")

    scale_factor = desired_serving/serving_size

    if scale_factor < 0.25:
        sf_ok = input("""Warning this scale is small,
accurate measurement of ingredients may be hard.
Do you want to keep going? Yes/No""").strip().lower()
        if sf_ok == "yes" or sf_ok == "y":
            scale_ok ="yes"

    elif scale_factor > 4:
        sf_ok = input("""Warning this scale is large,
be aware you have enough space for all ingredients.
Do you want to keep going? Yes/No""").strip().lower()
        if sf_ok == "yes" or sf_ok == "y":
            scale_ok ="yes"
    else:
        print("Scale factor: {:.2f}".format(scale_factor))
        scale_ok = "yes"

# loop for ingredients
stop= ""
while stop != "xxx":
    ingredient = not_blank("Please enter the ingredient: ","yes")
    if ingredient == "xxx" and len(ingredient_list)>=2:
        break
    elif ingredient == "xxx" and len(ingredient_list)<2:
        print("Please enter more than 2 ingredients")
    elif ingredient in ingredient_list:
        print("You have already entered this ingredient, Please enter another")
    else:
        amount = num_check("How much? ")
        scaled = amount * scale_factor

        # rounding
        if scaled % 1 == 0:
            scaled = round(scaled)
        elif scaled * 10 % 1 == 0:
            scaled ="{:.1f}".format(scaled)
        else:
            scaled = "{:.2f}".format(scaled)

        ingredient_list.append([ingredient,amount,scaled])

# print list unit then ingredient
for item in ingredient_list:
    print(item[2],item[0])
