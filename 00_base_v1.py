# imports

# functions & methods
# check input is not blank/ has digits
def not_blank(question):
    valid = False
    while not valid:
        # ask user for entry and assesses if not blank
        response = input(question).strip().lower()
        if response.isdigit():
            print("Entry cannot have numbers please try again")
            valid = False
        elif response != "":
            return response
            valid = True

        else:
            print("Entry cannot be blank")

# check input is a whole number between 1-20
def int_check(question,error):

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if response > 0 and response <= 20:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# check input is yes or no
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


# main routine
# ask user recipe name and source
recipe_name = not_blank("What is the name of your recipe? ")
recipe_source = not_blank("Where did you get your recipe from? ")

# ask user amount of serving and desired serve
total_serving = int_check("How many serves does the current recipe make? ","Please enter a max serving of 20 ")
desired_serving = int_check("How many serve of your recipe do you want to make? ", "Please enter a whole number")

# print for testing
print("You chose {} from {} which makes {} portions".format(recipe_name,recipe_source,total_serving))
serving_confirmation = yes_no("You wish to make {} portions. Is that correct? ".format(desired_serving))

